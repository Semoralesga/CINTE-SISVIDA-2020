from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Cyclist, CyclingTeam


engine = create_engine('sqlite:///franceTour.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

newCyclingTeam = CyclingTeam(name="INEOS Grenadiers", victories=76)
session.add(newCyclingTeam)
session.commit()
newCyclist = Cyclist(name="Egan Bernal", nationality="Colombiana", salary="1000000", cycling_team=newCyclingTeam)
session.add(newCyclist)
session.commit()

newCyclingTeam = CyclingTeam(name="Team Jumbo-Visma", victories=70)
session.add(newCyclingTeam)
session.commit()
newCyclist = Cyclist(name="Primoz Roglic", nationality="Eslovena", salary="1100000", cycling_team=newCyclingTeam)
session.add(newCyclist)
session.commit()

newCyclingTeam = CyclingTeam(name="Deceuninck - Quick Step", victories=81)
session.add(newCyclingTeam)
session.commit()
newCyclist = Cyclist(name="Sam Bennett", nationality="Irlandes", salary="900000", cycling_team=newCyclingTeam)
session.add(newCyclist)
session.commit()

newCyclingTeam = CyclingTeam(name="Movistar Team", victories=67)
session.add(newCyclingTeam)
session.commit()
newCyclist = Cyclist(name="Alejandro Valverde", nationality="Espanola", salary="950000", cycling_team=newCyclingTeam)
session.add(newCyclist)
session.commit()

newCyclingTeam = CyclingTeam(name="EF Pro Cycling", victories=53)
session.add(newCyclingTeam)
session.commit()
newCyclist = Cyclist(name="Rigoberto Uran", nationality="Colombiana", salary="800000", cycling_team=newCyclingTeam)
session.add(newCyclist)
session.commit()


