import subprocess
from livekit.agents import function_tool
from features.explanation import set_last_action


@function_tool()
async def energy_saver_on() -> str:
    """
    Turn Battery Saver (Energy Saver) ON.
    """
    subprocess.run(
        ["powercfg", "/setdcvalueindex", "SCHEME_CURRENT",
         "SUB_ENERGYSAVER", "ESBATTTHRESHOLD", "100"],
        capture_output=True,
        text=True
    )
    subprocess.run(
        ["powercfg", "/setactive", "SCHEME_CURRENT"],
        capture_output=True,
        text=True
    )
    set_last_action("Turned on energy saver.")
    return "Energy saver turned on."


@function_tool()
async def energy_saver_off() -> str:
    """
    Turn Battery Saver (Energy Saver) OFF.
    """
    subprocess.run(
        ["powercfg", "/setdcvalueindex", "SCHEME_CURRENT",
         "SUB_ENERGYSAVER", "ESBATTTHRESHOLD", "0"],
        capture_output=True,
        text=True
    )
    subprocess.run(
        ["powercfg", "/setactive", "SCHEME_CURRENT"],
        capture_output=True,
        text=True
    )
    set_last_action("Turned off energy saver.")
    return "Energy saver turned off."
