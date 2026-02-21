import subprocess
from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool()
async def scan_bluetooth_devices() -> str:
    """
    Best-effort scan of Bluetooth devices.
    Lists available Bluetooth devices known to Windows.
    """
    cmd = (
        "powershell -Command "
        "\"Get-PnpDevice | "
        "Where-Object {$_.Class -eq 'Bluetooth' -and $_.Status -eq 'OK'} "
        "| Select-Object -ExpandProperty FriendlyName\""
    )

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    devices = [d.strip() for d in result.stdout.splitlines() if d.strip()]

    if not devices:
        return "No Bluetooth devices found."
    
    set_last_action("Scanned for Bluetooth devices")
    return "Bluetooth devices found: " + ", ".join(devices)


@function_tool()
async def open_bluetooth_ui() -> str:
    """
    Open Bluetooth settings UI so user can turn ON/OFF or connect/disconnect.
    """
    subprocess.run(
        ["cmd", "/c", "start", "ms-settings:bluetooth"],
        shell=True
    )
    
    set_last_action("Opened Bluetooth settings")
    return "Bluetooth settings opened."
