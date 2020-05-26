from .models import User

from .extensions import ma


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


user_schema = UserSchema()
users_schema = UserSchema(many=True)