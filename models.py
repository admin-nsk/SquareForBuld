from sqlalchemy import create_engine, Column, Float, \
    Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


db = create_engine('sqlite:///locationForBuild.db', echo=False)
Base = declarative_base()


class Location(Base):
    """Table squares"""
    
    __tablename__ = 'locations'
    id = Column(Integer, primary_key = True)
    longitude = Column(Float)
    latitude = Column(Float)
    id_location = Column(Integer)
    address = Column(String)
    area = Column(Float)
    having_houses = Column(ForeignKey('having_houses.id'))


class Flat(Base):
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
    building = Column(ForeignKey('buildings.id'))


class Having_Houses(Base):
    """Table list"""
    __tablename__ = 'having_houses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Confluence(Base):
    """Table confluence building and location"""
    __tablename__ = 'confluences'
    id = Column(Integer, primary_key=True)
    flat = Column(ForeignKey('flats.id'))
    location = Column(ForeignKey('locations.id'))


class Building(Base):
    """Table Building"""
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    count_floor = Column(Integer)
    count_offer = Column(Integer)
    year_build = Column(Integer)
    location = Column(ForeignKey('locations.id'))


if __name__ == '__main__':
    Base.metadata.create_all(db)
