from decimal import Decimal

from pony.orm import Database, Required, PrimaryKey, Optional, Set
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class Location(db.Entity):
    """Table squares"""
    id = PrimaryKey(int, auto=True)
    longitude = Required(Decimal)
    latitude = Required(Decimal)
    id_location = Required(int)
    address = Optional(str)
    area = Required(Decimal)


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


class Сonfluence(db.Entity):
    id_flat = Set(Flats)
    id_location = Set(Location)