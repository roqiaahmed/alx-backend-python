#!/usr/bin/python3

seed = __import__("seed")


connection = seed.connect_to_prodev()


def stream_users_in_batches(batch_size):
    cur = connection.cursor()
    cur.execute("SELECT * FROM user_data")

    con = True
    while con:
        users = cur.fetchmany(batch_size)
        if len(users) >= 1:
            yield users
        else:
            cur.close()
            con = False


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user[3] >= 25:
                print(user)
                return user
