import json

from app.extensions import db
from datetime import datetime


class Serializable:
    def serialize(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }

    def to_json(self):
        return json.dumps(self.serialize())


class BaseModel(Serializable, db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, onupdate=datetime.utcnow)
