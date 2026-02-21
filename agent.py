from dotenv import load_dotenv
import asyncio
import logging

from livekit import agents
from livekit.agents import AgentSession, Agent
from livekit.plugins import google

# ---- Feature Imports ----
from features.prompts import AGENT_INSTRUCTION as behavior_prompts
from features.prompts import SESSION_INSTRUCTION
from features.weather import get_weather
from features.google_search import google_search
from features.Apps import (
    open_app, close_app,
    maximize_window, minimize_window,
    restore_window, focus_window,
    open_folder, close_folder
)
from features.jarvis_control import shutdown_jarvis
from features.screenshot import take_screenshot
from features.volume import set_volume
from features.battery import battery_status
from features.datetime import current_time, current_date
from features.web import open_website
from features.maps import open_google_maps
from features.youtube import search_youtube, play_youtube_video
from features.explanation import explain_last_action
from features.auto_code import open_code_in_notepad
from features.wifi import wifi_on, wifi_off, scan_wifi, connect_wifi, disconnect_wifi
from features.bluetooth import scan_bluetooth_devices, open_bluetooth_ui
from features.energy_saver import energy_saver_on, energy_saver_off
from features.brightness import set_brightness, brightness_up, brightness_down
from memory.memory_tools import remember_fact, recall_fact
from features.media_control import pause_media, play_media, next_media, previous_media

# ---- Setup ----
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---- Assistant Definition ----
class Assistant(Agent):
    def __init__(self):
        super().__init__(
            instructions=behavior_prompts,
            tools=[
                # Core
                get_weather,
                google_search,
                shutdown_jarvis,
                take_screenshot,
                set_volume,
                battery_status,
                current_time,
                current_date,
                open_website,
                open_google_maps,

                # YouTube
                search_youtube,
                play_youtube_video,

                # Code
                open_code_in_notepad,

                # WiFi
                wifi_on, wifi_off,
                scan_wifi,
                connect_wifi, disconnect_wifi,

                # Bluetooth
                scan_bluetooth_devices,
                open_bluetooth_ui,

                # Energy
                energy_saver_on,
                energy_saver_off,

                # Brightness
                set_brightness,
                brightness_up,
                brightness_down,

                # Window & Apps
                open_app, close_app,
                maximize_window, minimize_window,
                restore_window, focus_window,
                open_folder, close_folder,

                # Memory
                remember_fact, recall_fact,

                # Media
                pause_media, play_media,
                next_media, previous_media,

                # Explanation
                explain_last_action,
            ]
        )


# ---- Entry Point ----
async def entrypoint(ctx: agents.JobContext):

    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            voice="Charon",
            temperature=0.5
        )
    )

    # Start session (clean version, no noise cancellation)
    await session.start(
        room=ctx.room,
        agent=Assistant(),
    )

    session.allow_interruptions = False

    @session.on("agent_speaking")
    def on_speaking():
        asyncio.create_task(session.audio_input.pause())

    @session.on("agent_done_speaking")
    def on_done():
        async def resume():
            await asyncio.sleep(0.3)
            await session.audio_input.resume()
        asyncio.create_task(resume())

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION,
    )

    # Keep worker alive
    await asyncio.Future()


# ---- Run Worker ----
if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
