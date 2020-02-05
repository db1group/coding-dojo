from flask import Flask
from flask_restful import Api

app = Flask('talk-scheduling')
api = Api(app)


@app.route('/', methods=['GET'])
def get():
    return "Server talk scheduling up"
