from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
import json
import uuid
import time

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose database
db = client['InfoSys']

# Choose collections
students = db['Students']
users = db['Users']

# Initiate Flask App
app = Flask(__name__)

users_sessions = {}

def create_session(username):
    user_uuid = str(uuid.uuid1())
    users_sessions[user_uuid] = (username, time.time())
    return user_uuid  

def is_session_valid(user_uuid):
    return user_uuid in users_sessions

# ΕΡΩΤΗΜΑ 1: Δημιουργία χρήστη
@app.route('/createUser', methods=['POST'])
def create_user():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "username" in data or not "password" in data:
        return Response("Information incompleted",status=500,mimetype="application/json")
    
    if users.find({"username":data["username"]}).count() == 0 :
        user = {"username": data['username'], "password": data['password']}
        # Add user to the 'users' collection
        users.insert_one(user)
        return Response(data['username']+" was added to the MongoDB",status=200,mimetype='application/json') 
    else:
        return Response("A user with the given username already exists",status=400,mimetype='application/json')

# ΕΡΩΤΗΜΑ 2: Login στο σύστημα
@app.route('/login', methods=['POST'])
def login():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "username" in data or not "password" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")


    user = users.find_one({"username":data['username']})
    if user == None:
        return Response('No student found with that username '+ data['username'] +' was found',status=500,mimetype='application/json')
    else:
        if user['password'] == data['password']:
            user_uuid = create_session(data['username'])
            res = {"uuid": user_uuid, "username": data['username']}
            return Response(json.dumps(res),status=200,mimetype='application/json') 
        else:
            return Response("Wrong username or password.",status=400,mimetype='application/json') 

# ΕΡΩΤΗΜΑ 3: Επιστροφή φοιτητή βάσει email 
@app.route('/getStudent', methods=['GET'])
def get_student():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        print("this is uuid: ",data['uuid'])
        print("this is email: ",data['email'])
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "email" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")


    print("this is uuid: ",data['uuid'])
    print("this is email: ",data['email'])
    #uuid = request.headers.get['authorization']   
    ans = is_session_valid(uuid)
    if ans == False:
        return Response("you have to login first or check your uuid",status=401)
    else:
        student = students.find_one({"email":data["email"]})
        if student == none:
            return Response("There is no student this this email"+ data["email"])
        else:
            return Response(json.dumps(student), status=200, mimetype='application/json')
   



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
