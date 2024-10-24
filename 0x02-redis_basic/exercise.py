#!/usr/bin/env python3
"""
This module defines the Cache class for interacting with Redis.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to interact with a Redis database.
    """

    def __init__(self):
        """
        Initializes the Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
