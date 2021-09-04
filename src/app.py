import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from routes import book, book_genre


app = FastAPI()
app.include_router(book.router)
app.include_router(book_genre.router)


if __name__ == "__main__":
    uvicorn.run("app:app", port=int(os.getenv('PORT')),
                reload=True, debug=True)