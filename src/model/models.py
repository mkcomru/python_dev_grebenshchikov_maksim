from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.model.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    login = Column(String, unique=True, index=True)

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner = relationship("User")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    header = Column(String, index=True)
    text = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    blog_id = Column(Integer, ForeignKey('blog.id'))
    author = relationship("User")
    blog = relationship("Blog")


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, index=True)
    user_id = Column(Integer, index=True)
    space_type_id = Column(Integer, ForeignKey('space_type.id'))
    event_type_id = Column(Integer, ForeignKey('event_type.id'))
    space_type = relationship("SpaceType")
    event_type = relationship("EventType")

class SpaceType(Base):
    __tablename__ = 'space_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class EventType(Base):
    __tablename__ = 'event_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
