import os
import sqlite3
from flask import Flask
import auth, assets
import db  
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev')  

if not os.path.exists("data.db"):
    print("Creating database...")
    db.init_db()

app.register_blueprint(auth.bp)
app.register_blueprint(assets.bp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)
