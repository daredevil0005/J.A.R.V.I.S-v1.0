import subprocess
from livekit.agents import function_tool
from features.explanation import set_last_action


# ---------- INTERNAL HELPER ----------
def _wifi_available() -> bool:
    """
    Check if Wi-Fi is actually available for use.
    Uses netsh wlan show interfaces (authoritative).
    """
    result = subprocess.run(
        ["netsh", "wlan", "show", "interfaces"],
        capture_output=True,
        text=True
    )

    output = result.stdout.lower()

    # When Wi-Fi is OFF, Windows returns:
    # "There is no wireless interface on the system."
    if "no wireless interface" in output:
        return False

    # If interface exists, Wi-Fi is ON (connected or disconnected)
    return "state" in output


# ---------- WIFI ON ----------
@function_tool()
async def wifi_on() -> str:
    subprocess.run(
        ["netsh", "interface", "set", "interface", "Wi-Fi", "enabled"],
        capture_output=True,
        text=True
    )
    set_last_action("Turned on Wi-Fi.")
    return "Wi-Fi enabled for network connections."


# ---------- WIFI OFF ----------
@function_tool()
async def wifi_off() -> str:
    subprocess.run(
        ["netsh", "interface", "set", "interface", "Wi-Fi", "disabled"],
        capture_output=True,
        text=True
    )
    set_last_action("Turned off Wi-Fi.")
    return "Wi-Fi disabled for network connections."


# ---------- SCAN WIFI ----------
@function_tool()
async def scan_wifi() -> str:
    output = subprocess.check_output(
        ["netsh", "wlan", "show", "networks", "mode=Bssid"],
        text=True,
        shell=True
    )

    networks = []
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("SSID") and ":" in line:
            ssid = line.split(":", 1)[1].strip()
            if ssid and ssid not in networks:
                networks.append(ssid)

    if not networks:
        return "No Wi-Fi networks found. Make sure Wi-Fi is turned on."

    return "Available Wi-Fi networks: " + ", ".join(networks)


# ---------- CONNECT WIFI ----------
@function_tool()
async def connect_wifi(ssid: str) -> str:
    if not _wifi_available():
        return "Wi-Fi is turned off. Please turn on Wi-Fi before connecting."

    result = subprocess.run(
        ["netsh", "wlan", "connect", f"name={ssid}"],
        capture_output=True,
        text=True,
        shell=True
    )

    if result.returncode == 0:
        set_last_action(f"Connected to Wi-Fi network: {ssid}.")
        return f"Connecting to {ssid}."
    
    return (
        f"Failed to connect to {ssid}. "
        "Make sure this Wi-Fi network is already saved on this PC."
    )

# ---------- DISCONNECT WIFI ----------
@function_tool()
async def disconnect_wifi() -> str:
    if not _wifi_available():
        return "Wi-Fi is already turned off."

    subprocess.run(
        ["netsh", "wlan", "disconnect"],
        capture_output=True,
        text=True,
        shell=True
    )
    set_last_action("Disconnected from the current Wi-Fi network.")
    return "Wi-Fi disconnected from the current network."
