from datetime import datetime

from .extensions import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    added_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.text

    @classmethod
    def findByUserId(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    def findUserItem(cls, id, user_id):
        return cls.query.filter_by(id=id, user_id=user_id).first()

    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def addItem(cls, text, user_id):
        item = cls(text=text, user_id=user_id)
        db.session.add(item)
        db.session.commit()
        return item

    def updateText(self, text):
        self.text = text
        db.session.commit()
        return self

    def updateCompleted(self, completed):
        self.completed = completed
        db.session.commit()
        return self

    def deleteItem(self):
        db.session.delete(self)
        db.session.commit()