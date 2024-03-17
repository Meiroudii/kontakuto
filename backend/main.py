from flask import request, jsonify
from config import app, db
from models import Contact, RealFriendList, Blacklist, SpecialList
from waitress import serve

# GET all json routes in blacklist
@app.route("/blacklist", methods=["GET"])
def get_blacklist():
    blacklist = Blacklist.query.all()
    json_blacklist = list(map(lambda x: x.to_json, blacklist))
    return jsonify({"blacklist": json_blacklist})

@app.route("/special-list", methods=["GET"])
def get_speciallist():
    speciallist = SpecialList.query.all()
    json_speciallist = list(map(lambda x: x.to_json, speciallist))
    return jsonify({"speciallist": json_speciallist})

# GET all json routes in friendlist | view
@app.route("/real-friends-list", methods=["GET"])
def get_friendlist():
    friendlist = RealFriendList.query.all()
    json_friendlist = list(map(lambda x: x.to_json, friendlist))
    return jsonify({"friendlist": json_friendlist})

# GET all json routes in contacts
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # Get all contacts that exists
    contacts = Contact.query.all()
    # Convert python objects to json
    json_contacts = list(map(lambda x: x.to_json, contacts))
    return jsonify({"contacts": json_contacts})

if __name__ == "__main__":
    # Instantiation here
    with app.app_context():
        db.create_all()

    print("\n\t\tServer is running! at localhost:8000\n")
    # app.run(debug=True)
    serve(app, host="0.0.0.0", port=8000)
    print("\n\t\tServer Stopped")
