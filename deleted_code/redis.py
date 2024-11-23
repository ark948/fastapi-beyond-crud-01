from aioredis import StrictRedis
from aioredis import Redis
from src.config import Config


# this is old and deprecated, (importing this will result in error)
token_blocklist = Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0
)


JTI_EXPIRY = 3600


# this puts token into blocklist
async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(
        name=jti,
        value="",
        exp=JTI_EXPIRY
    )


# this checks if token is in blocklist
async def token_in_blocklist(jti: str) -> bool:
    jti = await token_blocklist.get(jti)
    return jti is not None