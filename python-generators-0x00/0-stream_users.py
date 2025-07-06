#!/usr/bin/python3

seed = __import__("seed")


connection = seed.connect_to_prodev()


def stream_users():
    cur = connection.cursor()
    cur.execute("SELECT * FROM user_data")
    for user in cur:
        yield user
