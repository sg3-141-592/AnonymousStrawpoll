from flask import Flask, request, json
from flask_socketio import SocketIO, join_room, leave_room, emit
import random_name
import database

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/createPoll', methods=['POST'])
def createPoll():
    data = request.json
    publicId = random_name.generate_name()
    
    newPoll = database.Poll(
        name = data['pollName'],
        options = {
            'one': data['optionOne'],
            'two': data['optionTwo']
        },
        userId = data['userId'],
        publicId = publicId
    )

    database.session.add(newPoll)
    database.session.commit()
    
    return json.dumps({
        'id': publicId
    }), 200

"""
Get a list of polls for a particular user
"""
@app.route('/getPolls', methods=['GET'])
def getPolls():
    return "OK", 200

@socketio.on('connect')
def get_connect():
    print("Client connected")

def getPollData(pollId):
    pollObject = database.session.query(database.Poll).filter_by(publicId=pollId).one()
    pollJson = {
        'name': pollObject.name,
        'options': pollObject.options
    }
    return json.dumps(pollJson)

@socketio.on('join')
def on_join(data):
    join_room(data['pollId'])
    currentUser = request.sid
    emit('update', getPollData(data['pollId']), to=currentUser)

if __name__ == '__main__':
    socketio.run(app, debug=True)
