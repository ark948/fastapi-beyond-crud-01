from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


def register_middleware(app: FastAPI):
    @app.middleware('http')
    async def authorization(request: Request, call_next):
        if not "Authorization" in request.headers:
            return JSONResponse(
                content={"message": "Not Authenticated",
                         "resolution": "Please provide the right credentials"},
                status_code=status.HTTP_403_FORBIDDEN
            )
        response = await call_next(request)
        return response
