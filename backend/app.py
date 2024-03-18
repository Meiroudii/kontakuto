from flask import request, jsonify
from config import app, db
from models import Contact, RealFriendList, Blacklist, SpecialList
from waitress import serve

# GET all json routes in blacklist
"""Blacklisted person route"""
@app.route("/blacklist", methods=["GET"])
def get_blacklist():
    blacklist = Blacklist.query.all()
    json_blacklist = list(map(lambda x: x.to_json, blacklist))
    return jsonify({"blacklist": json_blacklist})

@app.route("/create-blacklist", methods=["POST"])
def create_blacklist():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    created_at = request.json.get("createdAt")
    updated_at = request.json.get("updatedAt")

"""Contacts person route"""
# GET all json routes in contacts
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # Get all contacts that exists
    contacts = Contact.query.all()
    # Convert python objects to json
    json_contacts = list(map(lambda x: x.to_json, contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create-contacts", methods=["POST"])
def create_contact():
    # getting the json file to validate the contact list
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    phone_number = request.json.get("phoneNumber")

"""SpecialList person route"""
@app.route("/special-list", methods=["GET"])
def get_speciallist():
    speciallist = SpecialList.query.all()
    json_speciallist = list(map(lambda x: x.to_json, speciallist))
    return jsonify({"speciallist": json_speciallist})

@app.route("/create-special-list", methods=["POST"])
def create_special_list():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    personality = request.json.get("personality")
    created_at = request.json.get("createdAt")
    updated_at = request.json.get("updatedAt")




"""RealFrieldlist person route"""
# GET all json routes in friendlist | view
@app.route("/real-friends-list", methods=["GET"])
def get_friendlist():
    friendlist = RealFriendList.query.all()
    json_friendlist = list(map(lambda x: x.to_json, friendlist))
    return jsonify({"friendlist": json_friendlist})

# Must test the api before working into frontend
@app.route("/create-real-friends-list", methods=["POST"])
def create_real_friendlist():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    age = request.json.get("age")
    favorite_food = request.json.get("favoriteFood")
    created_at = request.json.get("createdAt")
    updated_at = request.json.get("updatedAt")

    # Check values if exist
    if not first_name or not last_name or not age or not favorite_food or not created_at or not updated_at:
        return (
                jsonify({"message": "You must include first name, last name, age, favorite food, created at, and update at"}),
                        400,

        )
    # If there's a valid data in database
    # create python class coresponding the columns of the database
    new_realfrieds = RealFriendList(
        first_name=first_name,
                last_name=last_name,
                age=age,
                favorite_food=favorite_food,
                created_at=created_at,
                updated_at=updated_at
        )
    # check if adding to the session of database is possible
    try:
        # staging area, ready to write into database, not yet saved
        db.session.add(new_realfrieds)
        # actuary write into database permanently
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "A new friend has been added!"}), 201



if __name__ == "__main__":
    # Instantiation here
    with app.app_context():
        db.create_all()

    print("\n\t\tServer is running! at localhost:8000\n")
    # app.run(debug=True)
    serve(app, host="0.0.0.0", port=8000)
    print("\n\t\tServer Stopped")
