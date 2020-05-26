from flask import jsonify, Response
from flask_restful import Resource, reqparse

from .models import User
from .schemas import user_schema


def validateEmailPassword(email, password):
    errors = {}
    if not email:
        errors['email'] = "Email is required field."
    if not password:
        errors['password'] = "Password is required field."
    return errors

def validateUser(first_name=None, last_name=None, email=None, password=None):
    errors = validateEmailPassword(email, password)
    if not first_name:
        errors['first_name'] = "First name is required field."
    if not last_name:
        errors['last_name'] = "Last name is required field."
    return errors


class Registration(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(trim=True, bundle_errors=True)
        self.parser.add_argument('email', type=str, required=True, help='Email is required field.', location='json')
        self.parser.add_argument('password', type=str, required=True, help='Password is required field.', location='json')
        self.parser.add_argument('first_name', type=str, required=True, help='First name is required field.', location='json')
        self.parser.add_argument('last_name', type=str, required=True, help='Last name is required field.', location='json')

    def post(self):
        args = self.parser.parse_args()

        errors = validateUser(**args)
        if errors:
            return errors, 400

        try:
            exists = bool(User.query.filter_by(email=args['email']).first())
            if exists:
                return {'message': 'Email already registered'}, 400

            user = User.createUser(**args)
            return user_schema.dump(user), 201
        except Exception as e:
            import traceback; traceback.print_exc()
            return {'error': str(e)}, 500
        return {'message': 'User registered successfully'}, 201


class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(trim=True, bundle_errors=True)
        self.parser.add_argument('email', type=str, required=True, help='Email is required field.', location='json')
        self.parser.add_argument('password', type=str, required=True, help='Password is required field.', location='json')
        

    def post(self):
        args = self.parser.parse_args()
        email = args['email']
        password = args['password']

        errors = validateEmailPassword(email, password)
        if errors:
            return errors, 400

        try:
            user = User.findUserByEmail(email)
            if not user:
                return {'message': 'Email is not registered.'}, 400
            elif user and user.isValidPassword(password):
                # You'll want to return a token that verifies the user in the future
                result = user_schema.dump(user)
                result.update({'token': user.token})
                return result, 200
            return {'error': 'User or password are incorrect'}, 401
        except Exception as e:
            import traceback; traceback.print_exc()
            return {'error': str(e)}, 500