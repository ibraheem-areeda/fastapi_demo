from fastapi import FastAPI

app = FastAPI(docs_url=None)


@app.get("/test")
def test_api():
    return {"hello": "test"}
