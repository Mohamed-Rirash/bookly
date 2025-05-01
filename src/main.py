from contextlib import asynccontextmanager

from fastapi import FastAPI

from books.routes import book_router
from db.db_conn import init_db

version = "0.1.0"

version_prefix = f"/api/{version}"


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    await init_db()
    yield
    print("server is off")


app = FastAPI(
    title="bookly",
    description="Simple book review system for books",
    version=version,
    lifespan=lifespan,
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(book_router)
