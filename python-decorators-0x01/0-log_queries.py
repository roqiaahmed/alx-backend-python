import logging
import sqlite3
import functools


#### decorator to lof SQL queries


def log_queries(func):

    def wrapper_log_queries(*args, **kwargs):
        for query in kwargs.get("query"):
            logging.info(query)
        return func(*args, **kwargs)

    return wrapper_log_queries


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
