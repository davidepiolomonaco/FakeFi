import subprocess
import re
from errors import NetworkError

def scanner(interface="wlan0"):
    try:
        scanner_result = subprocess.run(
            ["sudo", "iwlist", interface, "scan"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if scanner_result.returncode != 0:
            raise NetworkError(f"[!] Scan failed: {scanner_result.stderr.strip()}")
        
        return parse_scan_result(scanner_result)
    
    except NetworkError as error:
        raise NetworkError(f"[!] Unexpected error during scan: {error}")


def parse_scan_result(network_scanned):
    networks = []
    ssid_regex = re.compile(r'SSID:"(.*?)"')
    bssid_regex = re.compile(r'Address: ([0-9A-Fa-f:]{17})')
    channel_regex = re.compile(r'Channel: (\d+)')
    
    ssid = ssid_regex.findall(network_scanned.stdout)
    bssid = bssid_regex.findall(network_scanned.stdout)
    channel = channel_regex.findall(network_scanned.stdout)
    
    for ssid, bssid, channel in zip(ssid, bssid, channel):
        networks.append({
            "SSID": ssid,
            "BSSID": bssid,
            "Channel": channel
        })
    
    return networks