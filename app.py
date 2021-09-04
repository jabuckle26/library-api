from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def get_hello_world():
    return {"data": "hi world"}


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)
