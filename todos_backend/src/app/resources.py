from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required

from .models import Item
from .schemas import items_schema, item_schema


class TodoList(Resource):
    method_decorators = [jwt_required]

    def __init__(self):
        self.parser =  reqparse.RequestParser(trim=True, bundle_errors=True)
        self.parser.add_argument('text', type=str, required=True, help='Item value is required.', location='json')

    def get(self):
        try:
            user = get_jwt_identity()
            user_id = user['id']
            items = Item.findByUserId(user_id)
            return items_schema.dump(items), 200
        except Exception as e:
            import traceback; traceback.print_exc()
            return {'error': str(e)}, 500
        return {'message': 'User registered successfully'}, 201

    def post(self):
        args = self.parser.parse_args()
        text = args.get('text')
        try:
            user = get_jwt_identity()
            user_id = user['id']
            item = Item.addItem(text, user_id)
            return item_schema.dump(item), 201
        except Exception as e:
            import traceback; traceback.print_exc()
            return {'error': str(e)}, 500


class TodoDetil(Resource):
    method_decorators = [jwt_required]

    def __init__(self):
        self.parser =  reqparse.RequestParser(trim=True, bundle_errors=True)
        self.parser.add_argument('text', type=str, required=False, location='json')
        self.parser.add_argument('completed', type=bool, required=False, location='json')

    def get(self, todo_id):
        try:
            user = get_jwt_identity()
            user_id = user['id']
            item = Item.findUserItem(todo_id, user_id)
            return item_schema.dump(item), 200
        except Exception as e:
            import traceback; traceback.print_exc()
            return {'error': str(e)}, 500
        return {'message': 'User registered successfully'}, 201

    def put(self, todo_id):
        args = self.parser.parse_args()
        print(args)
        text = args.get('text')
        completed = args.get('completed')
        try:
            user = get_jwt_identity()
            user_id = user['id']
            item = Item.findUserItem(todo_id, user_id)
            if not item:
                return {'message': 'Item not exists'}
            if completed is not None:
                item = item.updateCompleted(completed)
            if text:
                item = item.updateText(text)
            return item_schema.dump(item), 201
        except Exception as e:
            import traceback; traceback.print_exc()
            return {'error': str(e)}, 500

    def delete(self, todo_id):
        try:
            user = get_jwt_identity()
            user_id = user['id']
            item = Item.findUserItem(todo_id, user_id)
            item.deleteItem()
            return {"message": "Item deleted successfully"}, 204
        except Exception as e:
            import traceback; traceback.print_exc()
            return {'error': str(e)}, 500