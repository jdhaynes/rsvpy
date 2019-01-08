from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from attendee import Attendee

Base = declarative_base()

class Event(Base):
    __tablename__ = 'rsvp_event'

    # Columns.
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    close_date = Column('close_date', DateTime)
    allow_tentative = Column('allow_tentative', Boolean)
    owner_id = Column('owner_id', Integer)
    date = Column('event_timestamp', DateTime)
    created_timestamp = Column('created_timestamp', DateTime)

    # Relationships.
    attendees = relationship(Attendee, primaryjoin=(id==Attendee.event_id), back_populates=Attendee.event)
    
    

