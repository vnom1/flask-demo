from flask import Flask
app = Flask(__name__)

app.config.from_pyfile("settings.py")
@app.route('/')
def index():
    return f'hello from flask'

@app.route('/dev/')
def dev():
    return f"hello:{app.config['SECRET_KEY']}"
 

