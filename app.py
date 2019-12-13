from weather import get_forecast
from flask import Flask



# I create a simple Flask server to display the weather data

app = Flask(__name__)

@app.route('/')
def home():
    s = "<h1><u>Upcoming Weather</u></h1>"
    weather = get_forecast()
    for w in weather:
        # utc_date = w['date_time']
        # # strftime format '%Y-%m-%d %H:%M:%S'
        # dt = datetime.strptime(utc_date, '%Y-%m-%d %H:%M:%S')
        # pac_dt = dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
        s += f"<p>Date/Time(PST): {w['date_time']} | Temp (F): {w['temp']}</p>"
    
    return s


if __name__ == "__main__":
    app.run(debug=True, port=8080)