#!/usr/bin/env python3
"""
This module defines the Cache class for interacting with Redis.
"""

import redis
import uuid
from typing import Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator to count how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the count for the method being called.
        """
        self._redis.incr(method.__qualname__)

        return method(self, *args, **kwargs)

    return wrapper


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

   @count_calls
   def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
   
   def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a value from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
