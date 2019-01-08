from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

Base = declarative_base()

class Attendee(Base):
    __tablename__ = 'rsvp_attendee'

    # Columns.
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    email = Column('email', String)
    secret = Column('attendee_secret' UUID(as_uuid=True), unique=True)
    response_id = Column('response_id', Integer)

    # Relationships.