from enum import Enum
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from app.config import DATABASE_URL

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session


class Status(Enum):
    PLANED = 'planed'
    ACTIVE = 'active'
    STOPPED = 'stopped'
    FINISHED = 'finished'
    ERROR = 'error'


class ModelType(Enum):
    NEW = 'new'
    SUCCESSFUL_BASIC_TESTS = 'successful basic tests'
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ERROR = 'error'


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    nikname = Column(String)
    created_at = Column(String)
    position = Column(String)
    last_login = Column(String, default=datetime.utcnow())


class Stream(Base):
    __tablename__ = 'stream'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    topic = Column(String)
    status = Column(String, default=Status.PLANED.value)
    created_at = Column(String, default=datetime.utcnow())


class AuthToken(Base):
    __tablename__ = 'auth_token'
    id = Column(Integer, primary_key=True)
    token = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(String, default=datetime.utcnow())


# class Model(Base):
#     __tablename__ = 'model'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     type = Column(String)
#     status = Column(String, default=Status.PLANED.value)
#     created_at = Column(String)
#
#
# class ReportLearn(Base):
#     __tablename__ = 'reportLearn'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     title = Column(String)
#     created_at = Column(String, default=datetime.utcnow())
