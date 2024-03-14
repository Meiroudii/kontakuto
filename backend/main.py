from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("greet/", methods=["GET"])

@app.route("easter-egg/", methods=["GET"])

@app.route("contacts/", methods=["GET"])
def get_contacts():
    # Get all contacts that exists
    contacts = Contact.query.all()

if __name__ "__main__":
    # Instantiation here
    with app.app_context():
        db.create_all()

    app.run(debug=True)
