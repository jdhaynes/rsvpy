from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from event import Event

Base = declarative_base()

class User(Base):
    __tablename__ = 'rsvp_user'

    # Columns.
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    email = Column('email', String)
    password_hash = Column('password_hash', String)
    password_salt = Column('password_salt', String)

    # Relationships.
    events = relationship(Event, primaryjoin=(id==Event.owner_id))