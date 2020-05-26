import os
import jwt

from datetime import datetime

from flask import Flask, request
from .extensions import api, cors, db, jwt, ma, migrate
from .resources import TodoList, TodoDetil


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # jwt extention config
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    app.config['JWT_TOKEN_LOCATION'] = os.environ.get('JWT_TOKEN_LOCATION', 'headers')
    app.config['JWT_HEADER_NAME'] = os.environ.get('JWT_HEADER_TYPE', 'Authorization')
    app.config['JWT_HEADER_TYPE'] = os.environ.get('JWT_HEADER_TYPE', 'jwt')

    # add resources api endpoints
    api.add_resource(TodoList, '/todos')
    api.add_resource(TodoDetil, '/todos/<int:todo_id>')


    # initialize all the extensions
    api.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World! - TODOs App'

    return app