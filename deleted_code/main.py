from fastapi import FastAPI, Header
from typing import Optional


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