import typer
import subprocess
from errors import AccessPointError

def setup(ssid, channel=6, interface="wlan0"):
    try:
        typer.echo(f"[...] Generating hostpad configuration")
        with open("/etc/hostpad/hostpad.conf", "w") as f:
            f.write(f"interface={interface}\n")
            f.write(f"driver=nl80211\n")
            f.write(f"ssid={ssid}\n")
            f.write(f"channel={channel}\n")
            f.write(f"hw_mode=g\n")
            f.write(f"auth_algs=1\n")
            f.write(f"ignore_broadcast_ssid=0\n")
        
        
        typer.echo("[...] Generating dnsmasq configuration")
        with open("/etc/dnsmasq.conf", "w") as f:
            f.write(f"interface={interface}\n")
            f.write("dhcp-range=192.168.1.2,192.168.1.100,12h\n")
            f.write("dhcp-option=3,192.168.1.1\n")
            f.write("dhcp-option=6,192.168.1.1\n")
            f.write("address=/#/192.168.1.1\n")
        
        
        typer.echo("[...] Setting IP address")
        subprocess.run(["sudo", "ifconfig", interface, "192.168.1.1", "netmask", "255.255.255.0", "up"], check=True)
            

        typer.echo("[...] Starting dnsmasq")
        subprocess.run(["sudo", "dnsmasq", "-C", "/etc/dnsmasq.conff"], check=True)
        
        
        typer.echo("[...] Starting hostpad")
        subprocess.run(["sudo", "hostpad", "/etc/hostapd/hostapd.conf"], check=True)
        
        
    except subprocess.CalledProcessError as subprocessError:
        raise AccessPointError(f"[!] Command failed: {subprocessError}")
    
    except AccessPointError as error:
        raise AccessPointError(f"[!] Failed to initialize access point: {error}")