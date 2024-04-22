import json
from redis_om import get_redis_connection
from core.config import Settings

redis = get_redis_connection(
    host="localhost",
    port="6379",
    decode_responses=True
)

def write_to_redis(key, value):
    redis.set(key, json.dumps(value))


def read_from_redis(key):
    return json.loads(redis.get(key))


