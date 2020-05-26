from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS


api = Api()
cors = CORS()
db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()