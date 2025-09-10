
#!/usr/bin/env python3
"""
Quickstart:
    python aus_nutrition_crawler.py --out data --max-pages 800 --depth 2

This script:
  1) Crawls *official* Australian nutrition/food-related sites (NHMRC, FSANZ, Dept of Health & Aged Care, ABS).
  2) Downloads HTML/PDF/DOCX docs within those domains.
  3) Extracts text and converts it into sentences.
  4) Writes JSONL/CSV suitable for RAG ingestion (with source metadata).

You can add/remove seed URLs with --seeds.
"""

import argparse
import csv
import io
import json
import os
import re
import sys
import time
from collections import deque
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Iterable, Optional, Set, Tuple
from urllib.parse import urldefrag, urljoin, urlparse

from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Optional deps for richer extraction
try:
    from pdfminer.high_level import extract_text as pdf_extract_text
except Exception:
    pdf_extract_text = None

try:
    import docx  # python-docx
except Exception:
    docx = None

# ---- Sentence splitting ----
_SENTENCE_END_RE = re.compile(
    r"(?<!\b[A-Z])[.!?]\s+(?=[A-Z0-9\"'(\[])"
)

def split_sentences(text: str) -> Iterable[str]:
    """
    Robust-ish splitter with graceful fallback to NLTK if available.
    """
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []

    # Try NLTK if present
    try:
        import nltk  # type: ignore
        try:
            _ = nltk.data.find("tokenizers/punkt")
        except LookupError:
            nltk.download("punkt", quiet=True)
        try:
            _ = nltk.data.find("tokenizers/punkt_tab")
        except LookupError:
            try:
                nltk.download("punkt_tab", quiet=True)
            except Exception:
                pass
        return nltk.sent_tokenize(text)
    except Exception:
        pass

    # Fallback: simple regex-based
    parts = _SENTENCE_END_RE.split(text)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if p and p[-1] not in ".!?":
            p = p + "."
        out.append(p)
    return out


ALLOWED_DOMAINS = {
    "www.nhmrc.gov.au",
    "nhmrc.gov.au",
    "www.fsanz.gov.au",
    "www.foodstandards.gov.au",  # FSANZ legacy
    "fsanz.gov.au",
    "www.health.gov.au",  # Department of Health and Aged Care
    "health.gov.au",
    "www.abs.gov.au",  # Australian Bureau of Statistics
    "abs.gov.au",
}

DEFAULT_SEEDS = [
    "https://www.health.gov.au/topics/food-and-nutrition",
    "https://www.nhmrc.gov.au/guidelines",
    "https://www.nrv.gov.au/",
    "https://www.foodstandards.gov.au/",
    "https://www.fsanz.gov.au/",
    "https://www.abs.gov.au/statistics/health/health-conditions-and-risks",
]

KEYWORDS = [
    # Keep this broad; it only prioritizes, doesn't strictly filter HTML pages
    "food", "nutrition", "nutrient", "diet", "dietary",
    "labelling", "labeling", "label", "standard", "guideline", "guidelines",
    "reference", "intake", "sodium", "salt", "sugar", "fat", "energy", "kilojoules",
    "fsanz", "nhmrc", "australian dietary guidelines", "nrv", "iron", "vitamin",
]

HTML_MIME = {"text/html", "application/xhtml+xml"}
PDF_MIME = {"application/pdf"}
DOCX_MIME = {"application/vnd.openxmlformats-officedocument.wordprocessingml.document"}


@dataclass
class Record:
    source_url: str
    doc_type: str
    title: str
    fetched_at: str
    sentence: str
    doc_path: Optional[str] = None


def is_allowed(url: str) -> bool:
    u = urlparse(url)
    return (u.scheme in {"http", "https"}) and (u.netloc in ALLOWED_DOMAINS)


def normalize_url(base: str, link: str) -> Optional[str]:
    if not link:
        return None
    abs_url = urljoin(base, link)
    abs_url, _frag = urldefrag(abs_url)
    if is_allowed(abs_url):
        return abs_url
    return None


def looks_relevant(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in KEYWORDS)


def fetch(session: requests.Session, url: str, timeout: int = 30) -> Tuple[Optional[bytes], Optional[str]]:
    try:
        resp = session.get(url, timeout=timeout, headers={"User-Agent": "aus-nutrition-rag/1.0"})
        if resp.status_code != 200:
            return None, None
        content_type = resp.headers.get("Content-Type", "").split(";")[0].strip().lower()
        return resp.content, content_type
    except Exception:
        return None, None


def extract_text_from_html(content: bytes, base_url: str) -> Tuple[str, str]:
    soup = BeautifulSoup(content, "lxml")
    # remove boilerplate
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "form", "aside"]):
        tag.decompose()
    title = soup.title.get_text(strip=True) if soup.title else urlparse(base_url).path.rsplit("/", 1)[-1]
    # concatenate main content
    text = soup.get_text(separator=" ", strip=True)
    return text, title or "Untitled"


def extract_text_from_pdf(content: bytes) -> str:
    if pdf_extract_text is None:
        # light fallback using PyPDF2 if available
        try:
            import PyPDF2  # type: ignore
            reader = PyPDF2.PdfReader(io.BytesIO(content))
            pages = [p.extract_text() or "" for p in reader.pages]
            return "\n".join(pages)
        except Exception:
            pass
        return ""
    # pdfminer
    with io.BytesIO(content) as bio:
        try:
            return pdf_extract_text(bio) or ""
        except Exception:
            return ""


def extract_text_from_docx(content: bytes) -> str:
    if docx is None:
        return ""
    try:
        f = io.BytesIO(content)
        document = docx.Document(f)
        return "\n".join(p.text for p in document.paragraphs if p.text)
    except Exception:
        return ""


def save_file(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        f.write(content)


def crawl_and_extract(out_dir: Path, seeds: Iterable[str], max_pages: int = 500, depth_limit: int = 2, strict_keyword_filter: bool = False):
    out_dir.mkdir(parents=True, exist_ok=True)
    session = requests.Session()

    visited: Set[str] = set()
    queue = deque([(s, 0) for s in seeds if is_allowed(s)])

    jsonl_path = out_dir / "sentences.jsonl"
    csv_path = out_dir / "sentences.csv"
    manifest_path = out_dir / "manifest.jsonl"

    jsonl_f = open(jsonl_path, "w", encoding="utf-8")
    csv_f = open(csv_path, "w", encoding="utf-8", newline="")
    manifest_f = open(manifest_path, "w", encoding="utf-8")

    csv_writer = csv.DictWriter(csv_f, fieldnames=["source_url", "doc_type", "title", "fetched_at", "sentence", "doc_path"])
    csv_writer.writeheader()

    fetched_count = 0
    discovered_docs = 0

    try:
        while queue and fetched_count < max_pages:
            url, depth = queue.popleft()
            if url in visited:
                continue
            visited.add(url)

            content, ctype = fetch(session, url)
            if content is None or not ctype:
                continue

            fetched_at = datetime.now(timezone.utc).isoformat()
            parsed = urlparse(url)
            ext = os.path.splitext(parsed.path.lower())[1]

            sentences = []
            title = ""
            doc_type = ""
            doc_local = None

            # HTML
            if ctype in HTML_MIME or ext in ("", ".html", ".htm", ".xhtml"):
                text, title = extract_text_from_html(content, url)
                if not text:
                    continue
                if strict_keyword_filter and not looks_relevant(text):
                    pass
                doc_type = "html"
                sentences = list(split_sentences(text))

                # Discover links for further crawl
                soup = BeautifulSoup(content, "lxml")
                for a in soup.select("a[href]"):
                    nurl = normalize_url(url, a.get("href"))
                    if not nurl or nurl in visited:
                        continue
                    if looks_relevant((a.get_text(" ") or "") + " " + a.get("href", "")) or not strict_keyword_filter:
                        if depth < depth_limit:
                            queue.append((nurl, depth + 1))

            # PDF
            elif ctype in PDF_MIME or ext == ".pdf":
                doc_type = "pdf"
                text = extract_text_from_pdf(content)
                title = os.path.basename(parsed.path) or "document.pdf"
                sentences = list(split_sentences(text))
                local_path = out_dir / "docs" / parsed.netloc / parsed.path.lstrip("/")
                save_file(local_path, content)
                doc_local = str(local_path)
            # DOCX
            elif ctype in DOCX_MIME or ext == ".docx":
                doc_type = "docx"
                text = extract_text_from_docx(content)
                title = os.path.basename(parsed.path) or "document.docx"
                sentences = list(split_sentences(text))
                local_path = out_dir / "docs" / parsed.netloc / parsed.path.lstrip("/")
                save_file(local_path, content)
                doc_local = str(local_path)
            else:
                continue

            discovered_docs += 1

            # Write manifest entry
            manifest = {
                "source_url": url,
                "doc_type": doc_type,
                "title": title,
                "fetched_at": fetched_at,
                "num_sentences": len(sentences),
            }
            manifest_f.write(json.dumps(manifest, ensure_ascii=False) + "\n")

            # Write sentence-level outputs
            for s in sentences:
                rec = Record(
                    source_url=url,
                    doc_type=doc_type,
                    title=title,
                    fetched_at=fetched_at,
                    sentence=s,
                    doc_path=doc_local,
                )
                jsonl_f.write(json.dumps(asdict(rec), ensure_ascii=False) + "\n")
                csv_writer.writerow(asdict(rec))

            fetched_count += 1

    finally:
        jsonl_f.close()
        csv_f.close()
        manifest_f.close()

    print(f"Visited pages: {len(visited)} | Documents processed: {discovered_docs} | See output files in {out_dir}.")


def main():
    p = argparse.ArgumentParser(description="Collect Australian official nutrition/food docs and split into sentences for RAG.")
    p.add_argument("--out", type=str, default="data", help="Output directory (default: data)")
    p.add_argument("--seeds", type=str, nargs="*", default=DEFAULT_SEEDS, help="Seed URLs to start crawling (must be within allowed government domains).")
    p.add_argument("--max-pages", type=int, default=500, help="Maximum number of pages/documents to process.")
    p.add_argument("--depth", type=int, default=2, help="Crawl depth limit for HTML pages.")
    p.add_argument("--strict-keyword-filter", action="store_true", help="If set, only follow/keep pages whose text/links look nutrition/food-related.")
    args = p.parse_args()

    out_dir = Path(args.out)
    crawl_and_extract(
        out_dir=out_dir,
        seeds=args.seeds,
        max_pages=args.max_pages,
        depth_limit=args.depth,
        strict_keyword_filter=args.strict_keyword_filter,
    )


if __name__ == "__main__":
    main()
