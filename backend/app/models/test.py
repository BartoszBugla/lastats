from app.extensions import db
from dataclasses import dataclass


@dataclass
class Test(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Test {self.name}>"
