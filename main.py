from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': "Hello World"}



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