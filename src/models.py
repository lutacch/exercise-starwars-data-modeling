import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    id = Column(Integer , primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(50), nullable=False)
    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer , primary_key=True)
    user_name = Column(String(250), nullable=False)
    user_from_id = Column(Integer, nullable=False)
    user_to_id = Column(Integer, nullable=False)

    def to_dict(self):
        return {}
   
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer , primary_key=True)
    user_name = Column(String(250), nullable=False)
    

    def to_dict(self):
        return {}
   
   
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer , primary_key=True)
    user_name = Column(String(250), nullable=False)
    text_inside = Column(String(250))

    def to_dict(self):
        return {}
   
   
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer , primary_key=True)
    user_name = Column(String(250), nullable=False)
    url = Column(String(250))
    post_id = Column(Integer)

    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
