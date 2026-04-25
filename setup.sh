#!/bin/bash

echo "Install Penguin Weather"
echo "This will install the app, icon, dependencies, and menu launcher."

read -p "Are you sure you want to continue? (y/n): " confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Install cancelled."
    exit 0
fi

APP_FOLDER="$HOME/rpi-penguinweather-app"
DESKTOP_FILE="$HOME/.local/share/applications/penguinweather.desktop"
ICON_DIR="$HOME/.local/share/icons"
ICON_FILE="$ICON_DIR/penguin.png"

echo "Installing dependencies..."

sudo apt update
sudo apt install -y python3-venv python3-tk fonts-noto-color-emoji

echo "Setting up Python environment..."

cd "$APP_FOLDER" || {
    echo "Error: Could not find app folder at $APP_FOLDER"
    exit 1
}

python3 -m venv venv
source venv/bin/activate
pip install requests

echo "Installing icon..."

mkdir -p "$ICON_DIR"
cp Icons/penguin.png "$ICON_FILE"

echo "Creating menu launcher..."

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

echo "Install complete."
echo "Penguin Weather should now appear in your Raspberry Pi OS menu."
echo "If the icon does not appear, reboot with:"
echo "sudo reboot"
