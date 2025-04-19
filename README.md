# FakeFi

💻 FakeFi is a Python tool designed to perform Evil Twin attacks by creating a fake WiFi Access Point and sending deauthentication packets to disconnect clients from the real network.

## Features

- 🔎 Wireless network scanning.
- 🎯 Target network selection.
- 📡 Fake Access Point creation.
- 💥 Deauthentication packet flood to force clients to connect to the fake AP.

## Requirements

- Python 3.9+
- `iwlist` (for WiFi scanning)
- `dnsmasq` (for DHCP/DNS management of the fake AP)
- `hostapd` (for creating the fake AP)
- `aireplay-ng` (for sending deauthentication packets)
- Root privileges (`sudo`)

## Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/davidepiolomonaco/FakeFi
cd fakefi
```

2️⃣ Install Python dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Make sure the following system packages are installed:
```bash
sudo apt-get install wireless-tools aircrack-ng dnsmasq hostapd
```

## Usage

Run the tool with:
```bash
sudo python3 main.py 
```

Follow the on-screen steps to:
- Select your WiFi interface.
- Pick a network to attack.
- Launch the Evil Twin attack.

## ⚠️ Disclaimer:

This project is for educational and testing purposes only in controlled environments you own.
Do not use it on third-party networks without explicit permission!