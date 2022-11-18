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
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    def to_dict(self):
        return {}
   

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer(250))
    hair_color = Column(String(10), nullable=False)
    skin_color = Column(String(10))
    eye_color = Column(String(50))
    birth_year = Column(Integer(8))
    gender = Column(String(10))


    def to_dict(self):
        return {}


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    rotation_period = Column(Integer(10))
    orbital_period = Column(Integer(10))
    diameter = Column(Integer(10))
    climate = Column(String(20))
    gravity = Column(String(30))
    terrain = Column(String(30))
    surface_water = Column(Integer(5))
    population = Column(Integer(100))
    def to_dict(self):
        return {}

class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    classification = Column(String(50))
    designation = Column(String(50))
    average_height = Column(Integer(50))
    skin_colors = Column(String(200))
    hair_colors = Column(String(200))
    average_lifespan = Column(Integer(50))
    language = Column(Integer(80))
    def to_dict(self):
        return {}

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(String(250), ForeignKey('character.id'))
    planet_id = Column((String(250)), ForeignKey('planet.id'))


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
