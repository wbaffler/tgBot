from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('2429e500637f679425e291cda7d9654e')
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=55.75222, lon=37.61556)

temp = str(one_call.forecast_daily[0].temperature('celsius').get('day', None)) 
status = str(one_call.forecast_daily[0].detailed_status) 
