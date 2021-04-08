from models import db, Locations, Flats, Confluences
from sqlalchemy.orm import sessionmaker
from math import radians, cos, sin, asin, sqrt
from logger_config import get_logger

log = get_logger('engine_logger')
log.setLevel('DEBUG')

Session = sessionmaker(bind=db)

def find_house_on_location():
  session_db = Session()
  #TODO вычисление нахождения дома на локации


def add_flat(data_flat):
  """
  data_flat - dict

  """
  session_db = Session()
  flat = Flats(**data_flat)
  session_db.add(flat)
  session_db.commit()

def add_location(data_location):
  """
  data_location - dict

  """
  session_db = Session()
  location = Locations(**data_location)
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

  R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

  distance_Lat = radians(coordinates['point_2_lat'] - coordinates['point_1_lat'])
  distance_Lon = radians(coordinates['point_2_lon'] - coordinates['point_1_lon'])
  coordinates['point_1_lat'] = radians(coordinates['point_1_lat'])
  coordinates['point_2_lat'] = radians(coordinates['point_2_lat'])

  a = sin(distance_Lat/2)**2 + cos(coordinates['point_1_lat'])*cos(coordinates['point_2_lat'])*sin(distance_Lon/2)**2
  result = 2*asin(sqrt(a))

  return R * result
