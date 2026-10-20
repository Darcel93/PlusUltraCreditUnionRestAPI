from logging import exception

import psycopg

from User import User

conn = psycopg.connect(
    host="localhost",
    port=5431,
    dbname="bank_db",
    user="darcel93",
    password= "password123",
    connect_timeout = 5
)

def login(username, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_name = %s AND password = %s; ", (username, password))
    result = cur.fetchone()
    if result is None:
        raise Exception("Invalid Username or Password")
    user = User(result[2], result[3], result[6], result[4], result[5], result[7], result[8], result[1])
    return user

def registration(profile_pic_url, first_name, last_name, email, user_name, password, account_number):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (profile_pic_url, first_name, last_name, email, user_name, password, account_number) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                (profile_pic_url,first_name, last_name, email, user_name, password, account_number))
    conn.commit()








