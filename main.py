from fastapi import FastAPI





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