# !/usr/bin/python3

import os

import uuid
import csv
from decimal import Decimal
from mysql import connector
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("MYSQL_USER")


def connect_db():
    try:
        connection = connector.connect(
            host="localhost",
            port=3307,
            user=USER,
            password=PASSWORD,
        )
        return connection
    except Exception as e:
        print(e)


def create_database(connection):
    cur = connection.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")


def connect_to_prodev():
    try:
        connection = connector.connect(
            host="localhost",
            user=USER,
            port=3307,
            password=PASSWORD,
            database="ALX_prodev",
        )
        return connection
    except Exception as e:
        print(e)


def create_table(connection):
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS user_data ("
        "user_id CHAR(36) PRIMARY KEY,"
        "name VARCHAR(255) NOT NULL,"
        "email VARCHAR(255) UNIQUE NOT NULL,"
        "age INT NOT NULL"
        ")"
    )
    print(f"Table user_data created successfully")


def insert_data(connection, data):
    cur = connection.cursor()
    with open_file(data) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                name, email, age = row
                user_id = str(uuid.uuid4())
                age = int(age)
                cur.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (user_id, name, email, age),
                )
            except Exception as e:
                print(e)
    # cur.execute("DELETE FROM user_data")

    connection.commit()


@contextmanager
def open_file(name):
    f = open(name, "r")
    try:
        yield f
    finally:
        f.close()
