import os
import requests
from livekit.agents import function_tool
from dotenv import load_dotenv
from features.explanation import set_last_action

load_dotenv()

@function_tool
async def get_weather(city: str = "") -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "Weather service is not configured."

    if not city:
        city = "Delhi"

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        res = requests.get(url, params=params, timeout=5)
        data = res.json()

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        set_last_action(f"Fetched weather information for {city}")


        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    except:
        return "Unable to fetch weather information."
