import webbrowser
from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool
async def open_google_maps(place: str) -> str:
    url = f"https://www.google.com/maps/search/{place.replace(' ', '+')}"
    webbrowser.open(url)
    set_last_action(f"Opened Google Maps for {place}")

    return f"Showing {place} on Google Maps."
