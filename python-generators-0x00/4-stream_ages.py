#!/usr/bin/python3

users = __import__("0-stream_users").stream_users


def stream_user_ages():
    for user in users:
        yield user[3]


def calculate_average():
    num_of_user = 0
    sum_of_age = 0
    for user in stream_user_ages():
        num_of_user += 1
        sum_of_age += user
    average_age = sum_of_age / num_of_user
    print(f"Average age of users: {average_age}")
