#!/bin/bash

echo "Uninstall Penguin Weather"
echo "This will remove the app, icon, and all data."

read -p "Are you sure you want to continue? (y/n): " confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Uninstall cancelled."
    exit 0
fi

APP_FOLDER="$HOME/rpi-penguinweather-app"
DESKTOP_FILE="$HOME/.local/share/applications/penguinweather.desktop"
ICON_FILE="$HOME/.local/share/icons/penguin.png"

echo "Uninstalling..."

# Remove launcher
if [ -f "$DESKTOP_FILE" ]; then
    rm "$DESKTOP_FILE"
    echo "Removed launcher"
fi

# Remove icon
if [ -f "$ICON_FILE" ]; then
    rm "$ICON_FILE"
    echo "Removed icon"
fi

# Remove app folder
if [ -d "$APP_FOLDER" ]; then
    rm -rf "$APP_FOLDER"
    echo "Removed app folder"
fi

echo "Uninstall complete."
echo "You may want to reboot to refresh the menu:"
echo "sudo reboot"
