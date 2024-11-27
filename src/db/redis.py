from redis import Redis
from src.config import Config

JTI_EXPIRY = 3600


redis_client = Redis.from_url(Config.REDIS_URL)



async def add_jti_to_blocklist(jti: str) -> None:
    print("REDIS TASK STARTED (adding token to blocklist)...")
    redis_client.set(name=jti, value="", ex=JTI_EXPIRY)
    print("REDIS TASK FINISHED.")



async def token_in_blocklist(jti: str) -> bool:
    jti = redis_client.get(jti)
    print("REDIS TASK (Token check)")
    return jti is not None
