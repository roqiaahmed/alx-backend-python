import time
import sqlite3
import functools

connection_module = __import__("1-with_db_connection")
with_db_connection = connection_module.with_db_connection

query_cache = {}


def cache_query(func):
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        result = query_cache.get(query)
        if result:
            return result
        query_cache[query] = func(*args, **kwargs)
        return query_cache[query]

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
