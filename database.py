from sqlalchemy import create_engine, Column, String, Integer, JSON, DateTime, ForeignKey, Float, func, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import logging
import datetime
import pandas as pd
import numpy as np

engine = create_engine('sqlite:///data.db', connect_args={"check_same_thread": False}, echo=False)

Base = declarative_base()

class Poll(Base):
    __tablename__ = 'polls'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    options = Column(JSON)
    userId = Column(String, index=True)
    created = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, index=True)
    publicId = Column(String, index=True)

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    pollId = Column(Integer, ForeignKey('polls.publicId'), index=True)
    userId = Column(String, index=True)
    created = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def getResamplingInterval(interval):
    # TODO: Add some proper rounding behaviour here
    return interval/10

"""
Get the votes over time for the poll
"""
def getAverageVoteData(pollId):
    averageData = []
    latestVote = {}

    for item in session.query(Vote.userId, Vote.value, Vote.created).filter_by(pollId=pollId):
        latestVote[item[0]] = item[1]
        average = 0
        for user in latestVote.keys():
            average += latestVote[user]
        average /= len(latestVote.keys())
        averageData.append({
            'y': average,
            'x': item[2]
        })
    
    if len(averageData) == 0:
        return [{
            'x': datetime.datetime.utcnow().timestamp(),
            'y': 0
        }]
    
    # Resample data
    df = pd.DataFrame(averageData)
    
    # Get the length of our dataset to work out resampling interval
    interval = df["x"].max() - df["x"].min()
    print("Interval", interval)
    # Add handling for an interval of 1
    if interval <= datetime.timedelta(seconds=1):
        return {
            'x': datetime.datetime.timestamp(df["x"][0]),
            'y': df["y"][0],
        }
    
    df = df.set_index('x')
    print("Resampling interval", getResamplingInterval(interval))
    resampled = df.resample(getResamplingInterval(interval), label='right').mean().dropna()
    outputData = []
    for index, row in resampled.iterrows():
        outputData.append({
            'x' : datetime.datetime.timestamp(index),
            'y' : row['y']
        })
    
    return outputData

"""
Get the latest votes for all of the users
"""
def getLatestVotes(pollId):

    subq = (
        session
        .query(Vote.id, Vote.userId, func.max(Vote.created).label("max_created"))
        .filter(Vote.pollId == pollId)
        .group_by(Vote.userId)
        .subquery()
    )

    q = (
        session.query(Vote)
        .join(subq, subq.c.id == Vote.id)
    )

    votes = []
    for item in q:
        votes.append(item.value)
    
    return votes
