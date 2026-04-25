# 🐧 Penguin Weather

A clean, simple weather dashboard for Raspberry Pi OS.

## 🌦️ Features
- Works worldwide (just type "City, Country")
- Save favourite locations
- 7-day forecast
- Desktop app (shows in Raspberry Pi menu)
- Custom icon included

---

## 📥 Installation (Raspberry Pi)

1. Clone the repo
git clone https://github.com/PenguinAlbert/rpi-penguinweather-app.git
cd rpi-penguinweather-app

2. Run the installer
chmod +x setup.sh
./setup.sh

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

## 📁 Project Structure

rpi-penguinweather-app/
main.py
Icons
    penguin.png
setup.sh
README.md
.gitignore

---

## Notes

- Favourites are stored locally (favourites.json)
- Not synced between devices
- Requires Raspberry Pi OS with desktop (GUI)

---

## 👤 Author

Made by PenguinAlbert
