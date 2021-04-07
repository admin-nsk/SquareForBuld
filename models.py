from sqlalchemy import create_engine, Column, Float, \
    Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


db = create_engine('sqlite:///locationForBuild.db', echo=True)
Base = declarative_base()


class Locations(Base):
    """Table squares"""
    
    __tablename__ = 'locations'
    id = Column(Integer, primary_key = True)
    longitude = Column(Float)
    latitude = Column(Float)
    id_location = Column(Integer)
    address = Column(String)
    area = Column(Float)
    having_houses = Column(ForeignKey('having_houses.id'))


class Flats(Base):
    """Table flats"""

    __tablename__ = 'flats'
    id = Column(Integer, primary_key=True)
    longitude = Column(Float)
    latitude = Column(Float)
    floor = Column(String)
    type_flat = Column(String)
    year_build = Column(Integer)
    material = Column(String)
    type_house = Column(String)
    number_of_room = Column(Integer)
    street = Column(String)


class Having_Houses(Base):
    """Table list"""
    __tablename__ = 'having_houses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Confluences(Base):
    """Table confluence building and location"""
    __tablename__ = 'confluences'
    id = Column(Integer, primary_key=True)
    id_flat = Column(ForeignKey('flats.id'))
    id_location = Column(ForeignKey('locations.id'))


Base.metadata.create_all(db)
