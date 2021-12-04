from flask import Flask, request, json, Response
from flask_socketio import SocketIO, join_room, leave_room, emit, rooms
import logging
import random_name
import database

import eventlet
eventlet.monkey_patch()

defaultLogger = logging.basicConfig(filename='errors.log', level=logging.INFO)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/createPoll', methods=['POST'])
def createPoll():
    data = request.json
    publicId = random_name.generate_name()
    
    newPoll = database.Poll(
        name = data['pollName'],
        options = {
            'one': data['optionOne'],
            'oneEmoji': data['optionOneEmoji'],
            'two': data['optionTwo'],
            'twoEmoji': data['optionTwoEmoji'],
        },
        userId = data['userId'],
        publicId = publicId
    )

    database.session.add(newPoll)
    database.session.commit()
    
    return Response(json.dumps({
            'id': publicId
        }),
        status=200,
        mimetype='application/json'
    )

"""
Get a list of polls for a particular user
"""
@app.route('/getPolls', methods=['GET'])
def getPolls():
    userId = request.args.get('userId')
    print(userId)
    polls = database.session.query(database.Poll).filter_by(userId=userId).order_by(database.Poll.created.desc())
    pollList = []
    for pollObject in polls:
        pollList.append({
            'name': pollObject.name,
            'url': pollObject.publicId
        })
    return Response(
        json.dumps(pollList),
        status=200,
        mimetype='application/json'
    )

@socketio.on('connect')
def get_connect():
    print("Client connected")

def getPollData(pollId, userId):
    # Check if user has any votes for poll
    latestVote = 0.5
    latestVoteQuery = database.session.query(database.Vote).\
        filter_by(pollId=pollId).\
        filter_by(userId=userId).order_by(database.Vote.created).first()
    if latestVoteQuery:
        latestVote = latestVoteQuery.value
    #
    pollObject = database.session.query(database.Poll).filter_by(publicId=pollId).one()
    pollJson = {
        'name': pollObject.name,
        'options': pollObject.options,
        'latestVote': latestVote,
    }
    return pollJson

@socketio.on('vote')
def vote(data):
    newVote = database.Vote(
        value = data['value'],
        pollId = data['pollId'],
        userId = data['userId']
    )
    database.session.add(newVote)
    database.session.commit()
    
    print("Vote update")
    emit('updateVotingDetails', database.getLatestVotes(data['pollId']), room=data['pollId'], json=True)
    emit('updateAnalyticsDetails', database.getAverageVoteData(data['pollId']), room=data['pollId'], json=True)

@socketio.on('join')
def on_join(data):
    pollId = data['pollId']
    join_room(pollId)
    currentUser = request.sid
    emit('updatePollDetails', getPollData(pollId, data['userId']), to=currentUser, json=True)
    emit('updateVotingDetails', database.getLatestVotes(pollId), to=currentUser, json=True)
    emit('updateAnalyticsDetails', database.getAverageVoteData(pollId), to=currentUser, json=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, log_output=True)
