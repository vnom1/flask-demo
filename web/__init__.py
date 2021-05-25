from flask import Flask
from web.runcmd import runcmd

cmd=['python -VVV','pip -VVV','pip freeze']

x=runcmd(cmd)

app = Flask(__name__)
@app.route('/')
def index():
    return f'hello from flask'

@app.route('/dev/')
def dev():
    return f"this is output{x[0]},this is error{x[1]}"

