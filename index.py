import requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/todos')
def getTodos():
    return requests.get('https://jsonplaceholder.typicode.com/todos').content

if __name__ == '__main__':
    app.run()