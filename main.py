from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional
from pydantic import BaseModel
from typing import List



app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str



class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str




@app.get('/')
async def read_root():
    return {'message': "Hello World"}


@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books


@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump() # converts it to dict
    books.append(new_book)
    return new_book

@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")


@app.patch('/book/{book_id}')
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")


@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

# path parameter
@app.get('/greet/{name}')
async def greet_name(name: str) -> dict:
    return {"message": f'Hello {name}'}
# http://127.0.0.1:8000/greet/john
# http://127.0.0.1:8000/greet/?name=wick



# query param
@app.get('/greet')
async def greet_name(name: str) -> dict:
    return {"message": f'Hello {name}'}
# http://127.0.0.1:8000/greet/?name=wick



# path and query param mixed
@app.get('/greet-v2/{name}')
async def greet_name_v2(name: str, age: int) -> dict:
    return {"message": f"hello {name}, age: {age}"}
# http://127.0.0.1:8000/greet-v2/?name=trevor?age=29





# path and query param mixed with default values
@app.get('/greet-v3')
async def greet_name_v3(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"hello {name}, age: {age}"}
# http://127.0.0.1:8000/greet-v3
# http://127.0.0.1:8000/greet-v3?name=trevor&age=70





class BookCreateModel(BaseModel):
    title: str
    author: str



@app.post('/create-book')
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }



# customizing headers
@app.get('/get-headers', status_code=200)
async def get_headers(
        accept: str = Header(None),
        content_type: str = Header(None),
        user_agent: str = Header(None),
        host: str = Header(None)
    ):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers