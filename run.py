import uvicorn, os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run("nutrihelp_ai.main:app", host="0.0.0.0", port=8000)
