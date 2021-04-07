from decimal import Decimal
from sqlalchemy import create_engine, Table, Column, Float, Integer, String, MetaData, ForeignKey


try:
    from settings import DB_CONFIG
except:
    exit("cannot open settings.py")


db = create_engine('sqlite:///Location.db:memory:', echo=True)
db.bind(**DB_CONFIG)

Base = declarative_base()


class Location(Base):
    """Table squares"""
    
    __tablename__ = 'location'
   id = Column(Integer, primary_key = True)
   longitude = Column(Float, nullable=False)
   latitude = Column(Float, nullable=False)
   id_location = Column(Integer, nullable=False)
   address = Column(String)
   area = Column(Float, nullable=False)
   having_houses = Column(ForeignKey('having_houses.id'))


class Flats(Base):
    """Table flats"""

   __tablename__ = 'flats'
   id = Column(Integer, primary_key = True)
   longitude = Column(Float, nullable=False)
   latitude = Column(Float, nullable=False) 
   floor = Column(String, nullable=False)
   type_flat = Column(String)
   year_build = Column(Integer)
   material = Column(String, nullable=False)
   type_house = Column(String)
   number_of_room = Column(Integer, nullable=False)
   street = Column(String, nullable=False)
      
class Having_Houses(Base):
    """Table list"""
    __tablename__ = 'having_houses'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)

class Confluence(db.Entity):
    """Table confluence building and location"""
    id_flat = Column(ForeignKey('flat.id'))
    id_location = Column(ForeignKey('location.id'))


Base.metadata.create_all(db)
