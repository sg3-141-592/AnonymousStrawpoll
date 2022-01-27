import datetime
import logging
import time
import os
import urllib

import numpy as np
import pandas as pd
from sqlalchemy import (JSON, Column, DateTime, Float, ForeignKey, Integer,
                        String, and_, create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

engine = None
if os.environ["DB_CONNECTION_STRING"].startswith("sqlite:"):
    engine = create_engine(
        os.environ["DB_CONNECTION_STRING"], connect_args={"check_same_thread": False}, echo=False
    )
else:
    engine = create_engine(
        "mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus(os.environ["DB_CONNECTION_STRING"]), echo=False
    )

Base = declarative_base()


class Poll(Base):
    __tablename__ = "polls"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    options = Column(JSON)
    userId = Column(String(100), unique=True)
    created = Column(
        DateTime(timezone=True), default=datetime.datetime.utcnow, index=True
    )
    publicId = Column(String(100), unique=True)


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    pollId = Column(String(100), ForeignKey("polls.publicId"), index=True)
    userId = Column(String(100), index=True)
    created = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


def getResamplingInterval(interval):
    dividedInterval = interval / 15
    resamplingInterval = dividedInterval.round(datetime.timedelta(
        seconds = 15
    ))
    if resamplingInterval > datetime.timedelta(seconds = 0):
        return resamplingInterval
    else:
        return dividedInterval


def getUserCount(pollId):
    result = session.query(Vote.userId).filter_by(pollId=pollId).distinct().count()
    return result

"""
Get the votes over time for the poll
"""
def getAverageVoteData(pollId):

    averageData = []
    latestVote = {}

    for item in session.query(Vote.userId, Vote.value, Vote.created).filter_by(
        pollId=pollId
    ):
        latestVote[item[0]] = item[1]
        average = 0
        for user in latestVote.keys():
            average += latestVote[user]
        average /= len(latestVote.keys())
        averageData.append({"y": average, "x": item[2]})
    
    outputData = {
        'averageData' : []
    }

    if len(averageData) == 0:
        outputData["averageData"].append({"x": datetime.datetime.utcnow().timestamp(), "y": 0.5})
    elif len(averageData) < 10:
        for row in averageData:
            outputData["averageData"].append({
                "x": datetime.datetime.timestamp(row["x"]),
                "y": row["y"]
            })
    else:
        # Resample data
        df = pd.DataFrame(averageData)

        # Get the length of our dataset to work out resampling interval
        interval = df["x"].max() - df["x"].min()

        df = df.set_index("x")
        resampled = (
            df.resample(getResamplingInterval(interval), label="right").mean().dropna()
        )

        # Remove the latest average point
        resampled.drop(resampled.tail(1).index, inplace=True)
        # Add the last latest average
        resampled.loc[averageData[-1]['x']] = [ averageData[-1]['y'] ]

        for index, row in resampled.iterrows():
            outputData["averageData"].append({"x": datetime.datetime.timestamp(index), "y": row["y"]})
    
    outputData["userCount"] = getUserCount(pollId)
    outputData["latestPoints"] = getLatestVotes(pollId)

    return outputData

"""
Get a list of polls the user has created or voted in
"""
def getUsersPolls(userId):
    subq = (
        session.query(Vote.pollId)
        .filter_by(userId=userId)
        .subquery()
    )

    votedPolls = session.query(Poll.name, Poll.publicId).join(subq, subq.c.pollId == Poll.publicId)

    createdPolls = session.query(Poll.name, Poll.publicId).filter_by(userId=userId)

    q = createdPolls.union(votedPolls)

    pollList = []
    for pollObject in q:
        pollList.append({"name": pollObject.name, "url": pollObject.publicId})
    return pollList

"""
Get the latest votes for all of the users on a poll
"""
def getLatestVotes(pollId):

    subq = (
        session.query(func.max(Vote.id).label("maxVoteId"))
        .filter(Vote.pollId == pollId)
        .group_by(Vote.userId)
        .subquery()
    )

    q = session.query(Vote.value, Vote.created).join(subq, subq.c.maxVoteId == Vote.id)

    votes = []
    for point in q:
        votes.append({
            'x': datetime.datetime.timestamp(point.created),
            'y': point.value
        })

    return votes
