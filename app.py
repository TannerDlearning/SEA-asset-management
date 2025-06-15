from flask import Flask
import auth, assets

app = Flask(__name__)
app.secret_key = 'dev'

app.register_blueprint(auth.bp)
app.register_blueprint(assets.bp)

if __name__ == '__main__':
    app.run(debug=True)
