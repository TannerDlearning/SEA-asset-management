import sqlite3
from flask import g

def get_connection():
    if 'db' not in g:
        g.db = sqlite3.connect("data.db")
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    with open('schema.sql') as f:
        db = sqlite3.connect("data.db")
        db.executescript(f.read())
        db.close()
