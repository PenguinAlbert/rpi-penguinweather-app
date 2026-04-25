# 🐧 Penguin Weather

A clean, simple weather dashboard for Raspberry Pi OS.

## 🌦️ Features
- Works worldwide (just type "City, Country")
- Save favourite locations
- 7-day forecast
- Desktop app (shows in Raspberry Pi menu)
- Custom icon included
- Universal install/uninstall commands

---

## 📥 Installation (Raspberry Pi)

1. Clone the repo

git clone https://github.com/PenguinAlbert/rpi-penguinweather-app.git

cd rpi-penguinweather-app

2. Run the installer

chmod +x setup.sh

./setup.sh

After installation, global commands will be available from anywhere.

---

## 🚀 Launching the App

After installing:

Go to:
Menu → Accessories → Penguin Weather

Or run manually:

cd ~/rpi-penguinweather-app

source venv/bin/activate 

python3 main.py

---

## 🧠 How to Use

Type a location like:
Sydney, Australia
London, UK
New York, USA

Click "Get Weather"

Click "Add Favourite" to save it

Click a favourite to load it

Use "Remove Favourite" to delete it

---

## ⚡ Universal Commands

After running the installer, you can use these commands from anywhere:

penguinweather-install

penguinweather-uninstall

---

## 💻 Compatibility

This app works on multiple operating systems as long as Python is installed.

### Supported Systems
- Raspberry Pi OS (fully supported with installer and menu integration)
- Linux (Ubuntu, Debian, etc.)
- macOS
- Windows

### Requirements
- Python 3
- Tkinter (usually included with Python)
- requests library

### Running on macOS / Linux / Windows

Install dependencies:

pip install requests

Run the app:

python main.py

### Notes
- The setup.sh installer only works on Raspberry Pi OS / Linux
- Menu integration (.desktop file) only works on Linux
- On macOS and Windows, the app must be run manually from the terminal

---

## 📁 Project Structure

rpi-penguinweather-app/
├── main.py
├── Icons/
│   └── penguin.png
├── setup.sh
├── uninstall.sh
├── penguinweather.desktop
├── README.md
├── .gitignore

---

## 🗑️ Uninstall

Run:

penguinweather-uninstall

Or manually:

chmod +x uninstall.sh

./uninstall.sh

---

## ⚠️ Notes

- Favourites are stored locally (favourites.json)
- Not synced between devices
- Requires Raspberry Pi OS with desktop (GUI) for full experience

---

## 💡 Future Ideas

- Auto-detect location
- Auto-refresh weather
- Better UI themes
- Cloud-synced favourites

---

## 👤 Author

Made by PenguinAlbert
