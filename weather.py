import os
from dotenv import load_dotenv
import requests as rq
from datetime import datetime,timezone

load_dotenv()

class weather:
    def __init__(self,lat,lon):
        
        params={
            'lat': lat,
            'lon': lon,
            'appid': os.getenv('API_KEY_WEATHER')
        }
        url ='https://api.openweathermap.org/data/2.5/weather?'
        response = rq.get(url,params=params)
        self.data = response.json()

    def getCurrentWeather(self):
        return self.data['weather'][0]['id'],self.data['weather'][0]['main']

    def getTime(self):
        sunrise= datetime.fromtimestamp(self.data['sys']['sunrise'],tz=timezone.utc).strftime("%H:%M:%S")
        sunset= datetime.fromtimestamp(self.data['sys']['sunset'],tz=timezone.utc).strftime("%H:%M:%S")
        return sunrise,sunset

climate = weather("-34.588963896613436","-58.47802856539185")
