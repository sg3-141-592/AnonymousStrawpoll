from flask import Flask, request, json
from flask_socketio import SocketIO
import random_name
import database

app = Flask(__name__)
socketio = SocketIO(app)

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

if __name__ == '__main__':
    socketio.run(app, debug=True)
