from datetime import datetime
from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool
async def current_time() -> str:
    set_last_action("Checked current time")
    return datetime.now().strftime("The time is %I:%M %p.")

@function_tool
async def current_date() -> str:
    set_last_action("Checked current date")
    return datetime.now().strftime("Today is %A, %d %B %Y.")
