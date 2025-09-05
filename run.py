import uvicorn, os

if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(
        "nutrihelp_ai.main:app",
        host="0.0.0.0",
        port=port,
        proxy_headers=True,
        forwarded_allow_ips="*",
        timeout_keep_alive=60
    )