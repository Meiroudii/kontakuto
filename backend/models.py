from config import db

class Contact(db.Model):
    # dbint pri true
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    favorite_food = db.Column(db.String(80), unique=False, nullable=False)

    # Pass through json API
    def to_json(self):
        return {
                "id": self.id,
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email,
                "phoneNumber": self.phone_number,
                "favoriteFood": self.favorite_food,
                }


