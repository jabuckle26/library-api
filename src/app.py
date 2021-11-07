import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import book, book_genre, borrowed_books, member


app = FastAPI()
app.include_router(book.router)
app.include_router(book_genre.router)
app.include_router(borrowed_books.router)
app.include_router(member.router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("app:app", port=int(os.getenv('PORT')),
                reload=True, debug=True)
