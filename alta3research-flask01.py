#!/usr/bin/env python3

"""This script is used for Project3 in ILT python class"""
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask import url_for
import sqlite3
import requests

app = Flask(__name__)
URL = "https://the-one-api.dev/v2/book/"
resp = requests.get(URL).json()
books = []
for book in resp["docs"]:
    books.append(book)

# Adds books to from api into a table


def add_to_db():
    con = sqlite3.connect('lotr.db')
    con.execute('''CREATE TABLE IF NOT EXISTS BOOKS
    (ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL);''')

    con.execute("INSERT INTO BOOKS (ID,NAME) VALUES (?,?)",
                (books[0]["_id"], books[0]["name"]))
    con.execute("INSERT INTO BOOKS (ID,NAME) VALUES (?,?)",
                (books[1]["_id"], books[1]["name"]))
    con.execute("INSERT INTO BOOKS (ID,NAME) VALUES (?,?)",
                (books[2]["_id"], books[2]["name"]))
    con.commit()

    con.close()

    return True


@app.route("/")
def home():
    return render_template("home.html")

# This endpoint will display the JSON from the lord of the rings API


@app.route("/lotr")
def lotr_json():
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
