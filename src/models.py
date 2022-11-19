import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer , primary_key=True)
    name = Column(Integer, ForeignKey("user.id"))
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(50), nullable=False)
    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer , primary_key=True)
    name = Column(Integer, ForeignKey("user.id"))
    user_name = Column(String(250), nullable=False)
    user_from_id = Column(Integer,ForeignKey("user.id"))
 

    def to_dict(self):
        return {}
   
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True )
    name = Column(Integer, ForeignKey("user.id"))
    user_name = Column(String(250), nullable=False)
    post = Column(String(500), ForeignKey("comment.id"))
    def to_dict(self):
        return {}
   
   
class Comment(Base):
    __tablename__ = 'comment'
    name = Column(Integer, ForeignKey("user.id"))
    id = Column(Integer, primary_key=True )
    user_name = Column(String(250), nullable=False)
    text_inside = Column(String(250))
    media = Column(String(250), ForeignKey("media.id"))

    def to_dict(self):
        return {}
   
   
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer , primary_key=True)
    user_name = Column(String(250), nullable=False)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("post_id"))

    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagramInstagram.png')
