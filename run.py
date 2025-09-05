import uvicorn, os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("nutrihelp_ai.main:app", host="127.0.0.1", port=port)
