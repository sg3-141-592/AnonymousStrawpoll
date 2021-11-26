from sqlalchemy import create_engine, Column, String, Integer, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import datetime

engine = create_engine('sqlite:///data.db')

Base = declarative_base()

class Poll(Base):
    __tablename__ = 'polls'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    options = Column(JSON)
    userId = Column(String, index=True)
    created = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    publicId = Column(String, index=True)


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
