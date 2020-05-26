import os

from flask import Flask
from flask_jwt_extended import jwt_required, get_jwt_identity

from .extensions import api, cors, db, jwt, migrate
from .resources import Registration, Login


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('USERS_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # jwt extention config
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    app.config['JWT_TOKEN_LOCATION'] = os.environ.get('JWT_TOKEN_LOCATION', 'headers')
    app.config['JWT_HEADER_NAME'] = os.environ.get('JWT_HEADER_TYPE', 'Authorization')
    app.config['JWT_HEADER_TYPE'] = os.environ.get('JWT_HEADER_TYPE', 'jwt')

    # add resources api endpoints
    api.add_resource(Registration, '/register')
    api.add_resource(Login, '/login')

    # initialize all the extensions
    api.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World! - USERs App'

    # # Protect a view with jwt_required, which requires a valid access token
    # # in the request to access.
    # @app.route('/protected', methods=['GET'])
    # @jwt_required
    # def protected():
    #     # Access the identity of the current user with get_jwt_identity
    #     current_user = get_jwt_identity()
    #     return jsonify(logged_in_as=current_user), 200


    return app