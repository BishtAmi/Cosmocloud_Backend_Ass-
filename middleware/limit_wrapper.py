from limits import RateLimitItem, RateLimitItemPerMinute, storage, strategies
import redis
from datetime import timedelta


REDIS_URL: str = "redis://localhost:6379/0"
redis_client = redis.Redis.from_url(REDIS_URL)
storage = storage.RedisStorage(REDIS_URL)
throttler = strategies.MovingWindowRateLimiter(storage)

"""
    This component is used as a wrapper for `limits`
"""


def hit(key: str, rate_per_minute: int, cost: int = 1) -> bool:
    """
        :param rate_per_minute: the number of request per minute to allow
        :return: returns `true` if a request can be passed and `false` if it needs to be blocked
    """
    item = rate_limit_item_for(rate_per_minute=rate_per_minute)
    is_hit = throttler.hit(item, key, cost=cost)
    # Set expiration time for the key in Redis (1 minute)
    redis_client.expire(key, timedelta(minutes=1))

    return is_hit


def rate_limit_item_for(rate_per_minute: int) -> RateLimitItem:
    # :param rate_per_minute: the number of request per minute to allow
    return RateLimitItemPerMinute(rate_per_minute)
