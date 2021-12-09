import eventlet
eventlet.monkey_patch()

from datetime import datetime
from random import randint, seed
import random_name
from flask import Flask, Response, json, request
from flask_socketio import SocketIO, emit, join_room

import database

seed(datetime.now())

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

URL_SUBFOLDER = "/api"

"""
Create new poll
"""
@app.route(URL_SUBFOLDER + "/createPoll", methods=["POST"])
def createPoll():
    data = request.json
    publicId = "{}-{}".format(random_name.generate_name(),randint(0,999))

    newPoll = database.Poll(
        name=data["pollName"],
        options={
            "one": data["optionOne"],
            "oneEmoji": data["optionOneEmoji"],
            "two": data["optionTwo"],
            "twoEmoji": data["optionTwoEmoji"],
        },
        userId=data["userId"],
        publicId=publicId,
    )

    database.session.add(newPoll)
    database.session.commit()

    return Response(
        json.dumps({"id": publicId}), status=200, mimetype="application/json"
    )


"""
Get a list of polls for a particular user
"""
@app.route(URL_SUBFOLDER + "/getPolls", methods=["GET"])
def getPolls():
    userId = request.args.get("userId")
    return Response(json.dumps(database.getUsersPolls(userId)), status=200, mimetype="application/json")


@socketio.on("connect")
def get_connect():
    print("Client connected")


def getPollData(pollId, userId):
    # Check if user has any votes for poll
    latestVote = 0.5
    latestVoteQuery = (
        database.session.query(database.Vote)
        .filter_by(pollId=pollId)
        .filter_by(userId=userId)
        .order_by(database.Vote.created)
        .first()
    )
    if latestVoteQuery:
        latestVote = latestVoteQuery.value
    pollObject = database.session.query(database.Poll).filter_by(publicId=pollId).one()
    pollJson = {
        "name": pollObject.name,
        "options": pollObject.options,
        "latestVote": latestVote,
    }
    return pollJson


@socketio.on("vote")
def vote(data):
    newVote = database.Vote(
        value=data["value"], pollId=data["pollId"], userId=data["userId"]
    )
    database.session.add(newVote)
    database.session.commit()

    emit(
        "updateVotingDetails",
        database.getLatestVotes(data["pollId"]),
        room=data["pollId"],
        json=True,
    )
    emit(
        "updateAnalyticsDetails",
        database.getAverageVoteData(data["pollId"]),
        room=data["pollId"],
        json=True,
    )


@socketio.on("join")
def on_join(data):
    pollId = data["pollId"]
    join_room(pollId)
    currentUser = request.sid
    emit(
        "updatePollDetails",
        getPollData(pollId, data["userId"]),
        to=currentUser,
        json=True,
    )
    # 
    emit(
        "updateAnalyticsDetails",
        database.getAverageVoteData(pollId),
        to=currentUser,
        json=True,
    )


if __name__ == "__main__":
    socketio.run(app, debug=True, log_output=True)
