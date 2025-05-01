from fastapi import APIRouter

book_router = APIRouter(
    prefix="/books",
)


@book_router.get("")
async def read_books():
    pass


@book_router.get("/{book_id}")
async def read_book(book_id):
    pass


@book_router.post("/")
async def create_book():
    pass


@book_router.put("/{book_id}")
async def update_book(book_id):
    pass


@book_router.delete("/{book_id}")
async def delete_book(book_id):
    pass
