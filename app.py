from flask import Flask, jsonify, Response, request
import pymongo
import json
from bson.objectid import ObjectId
import jwt
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = "tentackles"

try:
    mongo = pymongo.MongoClient(
        host='localhost',
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.tentackles
    mycol = db.users


except:
    print("There is a error while creating the Database")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = mycol.find({"name": data["name"]})

        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route("/api/v1/auth/signup", methods=["POST"])
def signup():
    
    try:
        user = {"name": request.form["name"], "email": request.form["email"],
                "mobile": request.form["mobile"], "password": request.form["password"]}
        dbResponse = mycol.insert_one(user)

        return Response(
            response=json.dumps(
                {"message": "user created",
                 "id": f"{dbResponse.inserted_id}"
                 }),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")


@app.route("/api/v1/auth/login", methods=["POST"])
def login():

    try:
        auth = {"name": request.form["name"],
                "password": request.form["password"]}
        login_user = mycol.find(auth)

        if login_user:
            token = jwt.encode(
                {"name": auth["name"]}, app.config['SECRET_KEY'])
            # print(token)
            return jsonify({"token": token.decode('UTF-8')})

        else:
            return "Incorrect credentials"

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")


@app.route("/api/v1/users", methods=["GET"])
@token_required
def get_all_users(current_user):
    
    try:
        data = list(mycol.find(
            {}, {"_id": 1, "name": 1, "email": 1, "mobile": 1}))

        for user in data:
            user["_id"] = str(user["_id"])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")
        return Response(
            response=json.dumps({"message": "cannot read user name"}),
            status=500,
            mimetype="application/json"
        )


@app.route("/api/v1/users/<user_id>", methods=["GET"])
@token_required
def get_user(current_user, user_id):
    
    try:
        data = list(mycol.find({"_id": ObjectId(user_id)}, {
                    "_id": 1, "name": 1, "email": 1, "mobile": 1}))

        for user in data:
            user["_id"] = str(user["_id"])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")
        return Response(
            response=json.dumps({"message": "cannot read user name"}),
            status=500,
            mimetype="application/json"
        )


if __name__ == "__main__":
    app.run(debug=True)
