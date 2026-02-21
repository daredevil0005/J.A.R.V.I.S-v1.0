import subprocess
from livekit.agents import function_tool
from features.explanation import set_last_action


@function_tool()
async def set_brightness(level: int) -> str:
    """
    Set screen brightness (0–100).
    """
    if level < 0 or level > 100:
        return "Brightness level must be between 0 and 100."

    cmd = (
        f"(Get-WmiObject -Namespace root/WMI "
        f"-Class WmiMonitorBrightnessMethods)"
        f".WmiSetBrightness(1,{level})"
    )

    subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True
    )

    return f"Brightness set to {level} percent."


@function_tool()
async def brightness_up() -> str:
    """
    Increase brightness by 10%.
    """
    cmd = (
        "$b=(Get-WmiObject -Namespace root/WMI "
        "-Class WmiMonitorBrightness).CurrentBrightness;"
        "$n=[Math]::Min($b+10,100);"
        "(Get-WmiObject -Namespace root/WMI "
        "-Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,$n)"
    )

    subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True
    )

    return "Brightness increased."


@function_tool()
async def brightness_down() -> str:
    """
    Decrease brightness by 10%.
    """
    cmd = (
        "$b=(Get-WmiObject -Namespace root/WMI "
        "-Class WmiMonitorBrightness).CurrentBrightness;"
        "$n=[Math]::Max($b-10,0);"
        "(Get-WmiObject -Namespace root/WMI "
        "-Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,$n)"
    )

    subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True
    )

    return "Brightness decreased."
