#!/bin/bash

APP_NAME="Penguin Weather"
APP_FOLDER="$HOME/rpi-penguinweather-app"
DESKTOP_FILE="$HOME/.local/share/applications/penguinweather.desktop"
ICON_DIR="$HOME/.local/share/icons"
ICON_FILE="$ICON_DIR/penguin.png"

echo "Installing Penguin Weather..."

cd "$APP_FOLDER" || {
  echo "Error: Could not find $APP_FOLDER"
  exit 1
}

sudo apt update
sudo apt install -y python3-venv python3-tk fonts-noto-color-emoji

python3 -m venv venv
source venv/bin/activate
pip install requests

mkdir -p "$ICON_DIR"
cp Icons/penguin.png "$ICON_FILE"

mkdir -p "$HOME/.local/share/applications"

cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Name=Penguin Weather
Comment=Weather dashboard app
Exec=$APP_FOLDER/venv/bin/python $APP_FOLDER/main.py
Icon=penguin
Terminal=false
Type=Application
Categories=Utility;
EOF

chmod +x "$DESKTOP_FILE"

echo "Done!"
echo "Penguin Weather should now appear in your Raspberry Pi OS menu."
echo "If the icon does not appear, reboot with: sudo reboot"
