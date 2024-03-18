from config import db
from datetime import datetime

class Blacklist(db.Model):
    # List of ...
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def to_json(self):
        return {
                "id": self.id,
                "firstName": self.first_name,
                "lastName": self.last_name,
                "createdAt": self.created_at,
                "updatedAt": self.updated_at
                }

class Contact(db.Model):
    # dbint pri true
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    # Pass through json API
    def to_json(self):
        return {
                "id": self.id,
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email,
                "phoneNumber": self.phone_number,
                }


class SpecialList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    personality = db.Column(db.String(80), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


    def to_json(self):
        return {
                "id": self.id,
                "firstName": self.first_name,
                "lastNme": self.last_name,
                "personality": self.personality,
                "createdAt": self.created_at,
                "updatedAt": self.updated_at
                }
class RealFriendList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=True)
    favorite_food = db.Column(db.String(80), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def to_json(self):
        return {
                "id": self.id,
                "firstName": self.first_name,
                "lastName": self.last_name,
                "age": self.age,
                "favoriteFood": self.favorite_food,
                "createdAt": self.created_at,
                "updatedAt": self.updated_at
                }
