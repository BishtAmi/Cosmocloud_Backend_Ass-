from typing import Callable, Awaitable, Any
from starlette.requests import Request 
from starlette.exceptions import HTTPException
from starlette.status import HTTP_429_TOO_MANY_REQUESTS 
from config.db import collection
from bson import ObjectId
from .limit_wrapper import hit

async def identifier(request: Request) -> str:
    user_id = request.path_params.get("id")
    print("user id:",user_id)
    existing_student = collection.find_one({"_id": ObjectId(user_id)})
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return user_id

async def _default_callback(request: Request):
    raise HTTPException(status_code=HTTP_429_TOO_MANY_REQUESTS, detail="request limit reached")

# only 5 request per minute
async def rate_provider(request: Request) -> str:
  return 5

class RateLimitMiddleware:
    def __init__(
        self,
        identifier: Callable[[Request], Awaitable[str]] = identifier,
        callback: Callable[[Request], Awaitable[Any]]= _default_callback,
        rate_provider: Callable[[Request], Awaitable[int]]=rate_provider
    ):
        self.identifier = identifier
        self.callback = callback
        self.rate_provider = rate_provider

    async def __call__(self, request: Request):
        callback = self.callback
        identifier = self.identifier
        rate_provider = self.rate_provider

        key = await identifier(request)
        rate = await rate_provider(request)

        if not hit(key=key, rate_per_minute=rate):
            return await callback(request)

# Instantiate RateLimitMiddleware with rate_provider argument
rate_limit = RateLimitMiddleware(rate_provider=rate_provider,identifier=identifier)
