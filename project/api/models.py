from sqlalchemy.sql import func

from project import db


class Account(db.Model):

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=func.now(), nullable=True)
    deleted_at = db.Column(db.DateTime, default=func.now(), nullable=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password
