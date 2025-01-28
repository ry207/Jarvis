import requests
import json
from api import api_key

def getWeather(location):

    # Go to https://www.tomorrow.io/weather-api/ for an api key
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"

    headers = {
        "accept": "application/json",
        "accept-encoding": "deflate, gzip, br"
    }

    try:

        response = requests.get(url, headers=headers)


        x = json.loads(response.text)

        y = x["data"]

        temp = y["values"]["temperature"]
        windspeed = y["values"]["windSpeed"]
        perc = y["values"]["precipitationProbability"]
        humidity = y["values"]["humidity"]
        loco = y["valie"]["location"]


        print(f"In {loco}:\n {temp}°\nHumidity: {humidity}\nWind speed: {windspeed} mph\nChance of precipitation: {perc}%\n")
    except:
        print("The request limit for this resource has been reached for the current rate limit window. Wait and retry the operation, or examine your API request volume.")


