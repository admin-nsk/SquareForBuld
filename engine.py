from models import Locations, Flats, Confluences

from logger_config import get_logger

log = get_logger('engine_logger')
log.setLevel('DEBUG')

def seach_location():
    log.warning(f'Мы пока не умеем обрабатывать события {event.type}')