from decimal import Decimal

from pony.orm import Database, Required, PrimaryKey, Optional, Set
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class Having_Houses(db.Entity):
    """Table list"""
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    locations = Set('Location', reverse='having_houses')


class Location(db.Entity):
    """Table squares"""
    id = PrimaryKey(int, auto=True)
    longitude = Required(Decimal)
    latitude = Required(Decimal)
    id_location = Required(int)
    address = Optional(str)
    area = Required(Decimal)
    confluence_location = Set('Confluence')
    having_houses = Optional(Having_Houses)


class Flats(db.Entity):
    """Table flats"""
    id = PrimaryKey(int, auto=True)
    longitude = Required(Decimal)
    latitude = Required(Decimal)
    floor = Required(str)
    type_flat = Optional(str)
    year_build = Optional(int)
    material = Required(str)
    type_house = Optional(str)
    number_of_room = Required(int)
    street = Required(str)
    confluence_flat = Set('Confluence')


class Confluence(db.Entity):
    """Table confluence building and location"""
    id_flat = Required(Flats, reverse='confluence_flat')
    id_location = Required(Location, reverse='confluence_location')






db.generate_mapping(create_tables=True)
