from datetime import datetime

from utils.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    # token = db.Column(db.String(255), unique=True)  # nullable=False,
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    profile_pic_url = db.Column(db.String(255))  # nullable=True)

    # def __init__(self, email):
    #     self.email = email

    def __init__(self, email, password, profile_pic_url):
        self.email = email
        self.password = password
        self.profile_pic_url = profile_pic_url

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'profile_pic_url': self.profile_pic_url
        }
