from fastapi import FastAPI

from books.routes import book_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(book_router)
