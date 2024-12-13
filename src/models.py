import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    created_at = Column(Integer)
    favorite_characters = relationship ('favorite_characters', backref="user")
    favorite_planets = relationship ('favorite_planets', backref="user")

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250))
    climate = Column(String(250))
    favorite_planets = relationship ('favorite_planets', backref="planets")

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    race = Column(String(250))
    planet = Column(String(250))
    favorite_characters = relationship ('favorite_characters', backref="characters")

class Favorite_characters(Base):
    __tablename__ = 'favorite_characters'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey ("characters.id"))
    user_id = Column(Integer, ForeignKey ("user.id"))

class Favorite_planets(Base):
    __tablename__ = 'favorite_planets'

    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey ("planets.id"))
    user_id = Column(Integer, ForeignKey ("user.id"))
    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')