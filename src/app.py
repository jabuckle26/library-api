import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_hello_world():
    return {"data": "hi world"}


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run("app:app", port=os.getenv('PORT'), reload=True)
