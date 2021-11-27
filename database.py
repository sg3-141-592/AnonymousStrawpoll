from sqlalchemy import create_engine, Column, String, Integer, JSON, DateTime, ForeignKey, Float, func, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import datetime

engine = create_engine('sqlite:///data.db', echo=False)

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

# class Analytics(Base):
#     __tablename__ = 'analytics'

#     id = Column(Integer, primary_key=True)
#     pollId = Column(Integer, ForeignKey('polls.publicId'), index=True)
#     value = Column(JSON())


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

"""
Get the votes over time for the poll
"""
def getAverageVoteData(pollId):
    labels = []
    data = []
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
            'x': datetime.datetime.timestamp(item[2])
        })
        labels.append(datetime.datetime.timestamp(item[2]))
        data.append(average)
    return averageData
    # return {
    #     'labels': labels,
    #     'data': data
    # }

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