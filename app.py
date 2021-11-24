from flask import Flask, request
from flask_socketio import SocketIO
import database

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/createPoll', methods=['POST'])
def createPoll():
    data = request.json
    print(data)
    
    newPoll = database.Poll(
        name = data['pollName'],
        options = {
            'one': data['optionOne'],
            'two': data['optionTwo']
        }
    )
    database.session.add(newPoll)
    database.session.commit()
    
    return "OK", 200


if __name__ == '__main__':
    socketio.run(app, debug=True)
