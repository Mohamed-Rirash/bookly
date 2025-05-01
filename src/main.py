from fastapi import FastAPI

from books.routes import book_router

version = "0.1.0"

version_prefix = f"/api/{version}"

app = FastAPI(
    title="bookly",
    description="Simple book review system for books",
    version=version,
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(book_router)
