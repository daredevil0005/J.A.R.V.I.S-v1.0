import psutil
from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool
async def battery_status() -> str:
    battery = psutil.sensors_battery()
    if not battery:
        return "Battery information is not available."

    status = "charging" if battery.power_plugged else "not charging"
    
    set_last_action("Checked battery status")
    return f"Battery is at {battery.percent} percent and {status}."
