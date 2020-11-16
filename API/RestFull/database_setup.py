from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



Base = declarative_base()

class CyclingTeam(Base):
    __tablename__ = 'cycling_team'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    victories = Column(Integer)

class Cyclist(Base):
    __tablename__ = 'cyclist'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    nationality = Column(String(20), nullable = False)
    salary = Column(String(8), nullable = False)
    cycling_team_id = Column(Integer, ForeignKey('cycling_team.id'))
    cycling_team = relationship(CyclingTeam)
    

engine = create_engine('sqlite:///franceTour.db')
Base.metadata.create_all(engine)
