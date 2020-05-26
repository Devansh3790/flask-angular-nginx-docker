from .models import Item

from .extensions import ma


class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item
        fields = ('id', 'text', 'completed', 'user_id', 'added_at')


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)