# api address pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{country code}
import json
import requests
from datetime import datetime, timezone


api_key = "e54be125738db08a265b496838886048"
city = "Los Angeles"
country_code = "US"

# Here I access the open weather api and return the 5 day/3 hour forecast for Los Angeles
source = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&units=imperial&APPID={api_key}'
response = requests.get(source)
data = json.loads(response.text)
data= data['list']

# Here I create a function to return the weather for a 24 hour period into my Flask 
# program to keep my code organized

def get_forecast():
    wl = []
    for d in data[:9]:
        weather_data = {}
        
        utc_date = d['dt_txt']
        # Here the date-time string is converted into a datetime object and the time zone is 
        # adjusted from utc to pst.
        dt = datetime.strptime(utc_date, '%Y-%m-%d %H:%M:%S')
        pac_dt = dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
        pac_dt = pac_dt.strftime('%Y-%m-%d %H:%M:%S')
        weather_data["date_time"] = pac_dt

        weather_data['temp'] = d['main']['temp']
        wl.append(weather_data)

    
    return wl

