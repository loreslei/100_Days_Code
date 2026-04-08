import requests
from datetime import datetime
import time
# import smtplib

MY_LAT = -5.028703
MY_LNG = -39.195722


def is_iss_overhead(your_lat, iss_lat, your_lng, iss_lng):
    if your_lat - 5 <= iss_lat <= your_lat + 5 and your_lng - 5 <= iss_lng <= your_lng + 5 :
        return True 
    return False
        
        
def get_api(api_url, api_params=None):
    response = requests.get(url=api_url, params=api_params)
    response.raise_for_status()
    data = response.json()
    return data


def is_night():
    parameters  = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0  
    }
    
    data = get_api(api_url='https://api.sunrise-sunset.org/json', api_params=parameters)
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True
    return False


data = get_api('http://api.open-notify.org/iss-now.json')

iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

iss_overhead = is_iss_overhead(your_lat=MY_LAT, your_lng=MY_LNG, iss_lat=iss_latitude, iss_lng=iss_longitude)

while True:
    time.sleep(60)
    if iss_overhead and is_night():
        print("The iss is above you!")
        




