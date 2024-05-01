from flask import flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

"""
from flask import Flask
from views import configure_routes

def create_app():
    app = Flask(__name__)
    configure_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
"""
