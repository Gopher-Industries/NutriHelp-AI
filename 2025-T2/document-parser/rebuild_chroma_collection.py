#!/usr/bin/env python3
import argparse
import hashlib
import json
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import chromadb

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from nutrihelp_ai.services.active_ai_backend import ActiveAISettings, _load_project_env

logger = logging.getLogger("rebuild_chroma_collection")

ALLOW_PREFIXES = [
    "https://www.health.gov.au/topics/food-and-nutrition",
    "https://www.foodstandards.gov.au/consumer/nutrition",
    "https://www.foodstandards.gov.au/consumer/labelling/nutrition",
    "https://www.foodstandards.gov.au/consumer/labelling/panels",
    "https://www.foodstandards.gov.au/consumer/food-fortification",
    "https://www.foodstandards.gov.au/science-data/food-nutrient-databases/afcd",
    "https://www.foodstandards.gov.au/science-data/food-nutrient-databases/ausnut/food-nutrients",
    "https://www.abs.gov.au/statistics/health/health-conditions-and-risks/australian-health-survey-nutrition-first-results-foods-and-nutrients",
    "https://www.abs.gov.au/statistics/health/health-conditions-and-risks/apparent-consumption-selected-foodstuffs-australia",
    "https://www.abs.gov.au/statistics/health/health-conditions-and-risks/national-health-measures-survey",
]

EXCLUDE_TITLE_TERMS = [
    "legal information",
    "data files",
    "frequently asked questions (afcd)",
    "resources",
    "homepage",
    "privacy",
    "food recalls",
    "food regulatory agencies",
]

BOILERPLATE_SUBSTRINGS = [
    "skip to main content",
    "listen print share",
    "funding find funding",
    "contact us",
    "download table as csv",
    "download graph as",
    "related resources companion resources",
    "annual compliance report",
    "temporary employment register",
    "food and nutrition topics food and nutrition",
    "nutrition | food standards australia new zealand skip to main content",
]

UTILITY_TERMS = [
    "nutrition",
    "nutrient",
    "healthy",
    "food group",
    "serve",
    "calcium",
    "iron",
    "protein",
    "vitamin",
    "mineral",
    "dairy",
    "legumes",
    "beans",
    "wholegrain",
    "fruit",
    "vegetable",
    "milk",
    "yoghurt",
    "cheese",
    "tofu",
    "fish",
    "meat",
    "eggs",
    "sardines",
    "diet",
    "kilojoules",
    "iodine",
    "folate",
    "magnesium",
    "sodium",
    "fat",
    "sugar",
]

TIME_PREFIX_RE = re.compile(r"^\d{2}:\d{2}\s")


def build_chroma_client(settings: ActiveAISettings):
    if settings.chroma_mode.lower() == "cloud":
        return chromadb.CloudClient(
            tenant=settings.chroma_tenant,
            database=settings.chroma_database,
            api_key=settings.chroma_api_key,
        )
    return chromadb.PersistentClient(path=settings.chroma_path)


def iter_records(path: Path) -> Iterable[Dict[str, str]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def sentence_is_useful(record: Dict[str, str]) -> bool:
    source_url = record.get("source_url", "").lower()
    title = record.get("title", "").lower()
    sentence = " ".join(record.get("sentence", "").split())
    lowered = sentence.lower()

    if not any(source_url.startswith(prefix) for prefix in ALLOW_PREFIXES):
        return False
    if any(term in title for term in EXCLUDE_TITLE_TERMS):
        return False
    if TIME_PREFIX_RE.match(sentence):
        return False
    if any(term in lowered for term in BOILERPLATE_SUBSTRINGS):
        return False
    if len(sentence) < 40 or len(sentence) > 500:
        return False
    if not any(term in lowered for term in UTILITY_TERMS):
        return False
    return True


def build_documents(
    sentences_path: Path,
    max_sentences_per_chunk: int = 5,
    max_chars_per_chunk: int = 1200,
) -> Tuple[List[str], List[Dict[str, object]], Dict[str, int]]:
    grouped: Dict[Tuple[str, str, Optional[str]], List[Dict[str, str]]] = defaultdict(list)

    for record in iter_records(sentences_path):
        if not sentence_is_useful(record):
            continue
        key = (
            record.get("title", "").strip(),
            record.get("source_url", "").strip(),
            record.get("doc_path"),
        )
        grouped[key].append(record)

    documents: List[str] = []
    metadatas: List[Dict[str, object]] = []

    for (title, source_url, doc_path), records in grouped.items():
        unique_sentences: List[str] = []
        seen_sentences = set()
        for record in records:
            sentence = " ".join(record.get("sentence", "").split())
            normalized = sentence.lower()
            if normalized in seen_sentences:
                continue
            seen_sentences.add(normalized)
            unique_sentences.append(sentence)

        chunk: List[str] = []
        chunk_len = 0
        chunk_index = 0

        for sentence in unique_sentences:
            additional = len(sentence) + 1
            if chunk and (
                len(chunk) >= max_sentences_per_chunk
                or chunk_len + additional > max_chars_per_chunk
            ):
                documents.append(
                    f"Title: {title}\nSource: {source_url}\n\n"
                    + " ".join(chunk)
                )
                metadatas.append(
                    {
                        "source_url": source_url,
                        "title": title,
                        "doc_path": doc_path or "",
                        "chunk_index": chunk_index,
                        "sentence_count": len(chunk),
                    }
                )
                chunk = []
                chunk_len = 0
                chunk_index += 1

            chunk.append(sentence)
            chunk_len += additional

        if chunk:
            documents.append(
                f"Title: {title}\nSource: {source_url}\n\n"
                + " ".join(chunk)
            )
            metadatas.append(
                {
                    "source_url": source_url,
                    "title": title,
                    "doc_path": doc_path or "",
                    "chunk_index": chunk_index,
                    "sentence_count": len(chunk),
                }
            )

    stats = {
        "documents": len(documents),
        "sources": len(grouped),
    }
    return documents, metadatas, stats


def backup_existing_collection(collection, backup_path: Path) -> int:
    count = collection.count()
    if count == 0:
        return 0

    payload = collection.get(include=["documents", "metadatas"])
    ids = payload.get("ids", [])
    documents = payload.get("documents", [])
    metadatas = payload.get("metadatas", [])

    backup_path.parent.mkdir(parents=True, exist_ok=True)
    with backup_path.open("w", encoding="utf-8") as handle:
        for idx, doc_id in enumerate(ids):
            record = {
                "id": doc_id,
                "document": documents[idx] if idx < len(documents) else "",
                "metadata": metadatas[idx] if idx < len(metadatas) else {},
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    return count


def rebuild_collection(
    client,
    collection_name: str,
    documents: List[str],
    metadatas: List[Dict[str, object]],
    backup_dir: Path,
    batch_size: int = 100,
) -> Dict[str, int]:
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / f"{collection_name}_backup.jsonl"

    try:
        existing = client.get_collection(name=collection_name)
        backed_up = backup_existing_collection(existing, backup_path)
        client.delete_collection(name=collection_name)
    except Exception:
        backed_up = 0

    collection = client.get_or_create_collection(name=collection_name)
    inserted = 0

    for start in range(0, len(documents), batch_size):
        docs_batch = documents[start : start + batch_size]
        metadata_batch = metadatas[start : start + batch_size]
        ids_batch = []
        for offset, (doc, metadata) in enumerate(zip(docs_batch, metadata_batch), start=start):
            raw_id = f"{metadata.get('source_url','')}|{metadata.get('chunk_index',0)}|{offset}"
            ids_batch.append(hashlib.sha1(raw_id.encode("utf-8")).hexdigest())
        collection.upsert(ids=ids_batch, documents=docs_batch, metadatas=metadata_batch)
        inserted += len(docs_batch)

    return {
        "backed_up": backed_up,
        "inserted": inserted,
        "final_count": collection.count(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean and rebuild the aus_food_nutrition Chroma collection.")
    parser.add_argument(
        "--sentences",
        default="2025-T2/document-parser/data/sentences.jsonl",
        help="Path to the source JSONL sentences file.",
    )
    parser.add_argument(
        "--collection",
        default=None,
        help="Override Chroma collection name. Defaults to RAG_COLLECTION from env.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print the filtered ingest summary without modifying Chroma.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Batch size for Chroma upserts.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    _load_project_env()
    settings = ActiveAISettings()

    sentences_path = Path(args.sentences).resolve()
    if not sentences_path.is_file():
        raise SystemExit(f"Sentences file not found: {sentences_path}")

    documents, metadatas, stats = build_documents(sentences_path)
    logger.info(
        "Prepared filtered nutrition corpus from %s (sources=%s chunks=%s)",
        sentences_path,
        stats["sources"],
        stats["documents"],
    )

    if args.dry_run:
        sample_count = min(3, len(documents))
        for idx in range(sample_count):
            logger.info("Sample chunk %s metadata=%s", idx + 1, metadatas[idx])
            logger.info("%s", documents[idx][:500])
        return 0

    client = build_chroma_client(settings)
    collection_name = args.collection or settings.rag_collection
    result = rebuild_collection(
        client=client,
        collection_name=collection_name,
        documents=documents,
        metadatas=metadatas,
        backup_dir=Path("2025-T2/document-parser/data/backups").resolve(),
        batch_size=args.batch_size,
    )
    logger.info(
        "Rebuilt collection %s (backed_up=%s inserted=%s final_count=%s)",
        collection_name,
        result["backed_up"],
        result["inserted"],
        result["final_count"],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
