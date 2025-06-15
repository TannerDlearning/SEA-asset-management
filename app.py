import os
import sqlite3
from flask import Flask
import auth, assets
import db  # this assumes you have a db.py with init_db() and get_connection()

app = Flask(__name__)
app.secret_key = 'dev'

# Automatically create and initialize database if it doesn't exist
if not os.path.exists("data.db"):
    print("Creating database...")
    db.init_db()

# Register routes
app.register_blueprint(auth.bp)
app.register_blueprint(assets.bp)

if __name__ == '__main__':
    app.run(debug=True)
