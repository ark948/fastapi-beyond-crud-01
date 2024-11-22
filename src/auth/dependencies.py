from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials
from src.auth.utils import decode_token



class AccessTokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        # auto_error will return the error instead of None
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        token = creds.credentials
        token_data = decode_token(token)
        if not self.token_valid:
            raise HTTPException(status_code=403, detail="Invalid or expired token")
        if token_data['refresh']:
            raise HTTPException(status_code=403, detail="Please provide an access token")
        return token_data
    
    def token_valid(self, token: str) -> bool:
        token_data = decode_token(token)
        return True if token_data is not None else False