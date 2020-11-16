from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

from .entity import Entity


Base = declarative_base()

class CyclingTeam(Entity, Base):
    __tablename__ = 'cycling_team'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    victories = Column(Integer)
    cyclist_number = Column(Integer, nullable = False)

    def __init__(self, name, cyclist_number, victories, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.cyclist_number = cyclist_number
        self.victories = victories


class CyclingTeamSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    cyclist_number = fields.Number()
    victories = fields.Number()
    created_at = fields.Str()
    updated_at = fields.Str()
    last_updated_by = fields.Str()


engine = create_engine('sqlite:///src/franceTour.db')
Base.metadata.create_all(engine)