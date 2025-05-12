from ISS import Iss
from weather import weather
from coordinates import Coordinates
from datetime import datetime
from message import message
import time

def main():
    ubication = input("Write your city: ")
    while True:
        # -------------- ISS POSITION --------------#
        iss = Iss()
        lat,lon = iss.getCoordinates()

        # -------------- USER POSITION --------------#
        user_coord = Coordinates(ubication) #<=== change for your a  Adress or City.
        x,y=user_coord.getCoordinates()

        # -------------- WEATHER --------------#
        forecast = weather(x,y)
        now = datetime.now().time()
        sunrise,sunset = forecast.getTime()
        id_climate,climate = forecast.getCurrentWeather()
        text = message()
        formatted_time = now.strftime("%H:%M:%S")

        # -------------- REACHABLE? --------------#
        if id_climate==800 and formatted_time>=sunset and formatted_time<=sunrise:    
            if x>=lat-5 and x<=lat+5 and y>=lon-5 and y<=lon+5:
                text.message_decision(id_climate)
                print("Waiting the next hour...")
                time.sleep(60*60)  
        elif formatted_time>=sunset and formatted_time<=sunrise:
            text.message_decision(id_climate-1)
            print("Waiting the next hours...")
            time.sleep(60*60)
        else:
            text.message_decision(id_climate-1)
            print("Waiting the next hours...")
            time.sleep(13*60*60)

if __name__=="__main__":
    main()