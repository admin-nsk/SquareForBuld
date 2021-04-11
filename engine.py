from models import db, Location, Flat, Confluence, Building
from sqlalchemy.orm import sessionmaker
from math import radians, cos, sin, asin, sqrt, pi
from logger_config import get_logger

log = get_logger('engine_logger')
log.setLevel('DEBUG')

Session = sessionmaker(bind=db)


def find_house_on_location():
    session_db = Session()
    locations = session_db.query(Location).all()
    buildings = session_db.query(Building).all()
    coordinates = {
        'point_1_lon': None,
        'point_1_lat': None,
        'point_2_lon': None,
        'point_2_lat': None
    }
    for location in locations:
        coordinates['point_1_lon'] = location.longitude
        coordinates['point_1_lat'] = location.latitude
        for building in buildings:
            coordinates['point_2_lon'] = building.longitude
            coordinates['point_2_lat'] = building.latitude
            distance = calculate_distance(coordinates)
            radius = calculate_radius(location.area)
            if radius >= distance:
                building.location = location.id
    session_db.commit()


def calculate_radius(S):
    return (sqrt(S)/pi)/1000


def add_flat(data_flat):
    """
  data_flat - dict

  """
    session_db = Session()
    flat = Flat(**data_flat)
    session_db.add(flat)
    session_db.commit()


def add_location(data_location):
    """
  data_location - dict

  """
    session_db = Session()
    location = Location(**data_location)
    session_db.add(location)
    session_db.commit()


def calculate_distance(coordinates):
    """
  coordinates = {
    'point_1_lon': 55.222132132,
    'point_1_lat': 85.222132132,
    'point_2_lon': 56.222132132,
    'point_2_lat': 86.222132132
  }
  """

    R = 6372.8  #  For Earth radius in kilometers use 6372.8 km

    distance_Lat = radians(coordinates['point_2_lat'] - coordinates['point_1_lat'])
    distance_Lon = radians(coordinates['point_2_lon'] - coordinates['point_1_lon'])
    point_1_lat = radians(coordinates['point_1_lat'])
    point_2_lat = radians(coordinates['point_2_lat'])

    a = sin(distance_Lat / 2) ** 2 + cos(point_1_lat) * cos(point_2_lat) * sin(
        distance_Lon / 2) ** 2
    result = 2 * asin(sqrt(a))

    return R * result

def add_building():
    session_db = Session()
    flats = session_db.query(Flat).all()
    for flat in flats:
        query = session_db.query(Building)\
            .filter(Building.address.in_([flat.street]))\
            .filter(Building.latitude.in_([flat.latitude]))\
            .filter(Building.longitude.in_([flat.longitude]))
        if not session_db.query(query.exists()).scalar():
            try:
                building = Building(
                    address=flat.street,
                    longitude=flat.longitude,
                    latitude=flat.latitude,
                    count_floor=int(flat.floor[flat.floor.index('/')+1:]),
                    year_build=flat.year_build
                )
                session_db.add(building)
            except:
                print('ex')

    session_db.commit()


def add_building_in_flat():
    session_db = Session()
    flats = session_db.query(Flat).all()
    for flat in flats:
        try:
            building = session_db.query(Building)\
                .filter(Building.address.in_([flat.street]))\
                .filter(Building.latitude.in_([flat.latitude]))\
                .filter(Building.longitude.in_([flat.longitude])).first()
            if building:
                flat.building = building.id
        except Exception as ex:
            log.debug(f'ex - {ex}')
    session_db.commit()


if __name__ == '__main__':
    find_house_on_location()
    # add_building()
    # add_building_in_flat()

