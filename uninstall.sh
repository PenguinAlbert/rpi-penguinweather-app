#!/bin/bash

echo "Uninstall Penguin Weather"
echo "This will remove the menu launcher, icon, and commands."
echo "Your repo folder will be kept so you can reinstall later."

read -p "Continue? (y/n): " confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Uninstall cancelled."
    exit 0
fi

DESKTOP_FILE="$HOME/.local/share/applications/penguinweather.desktop"
ICON_FILE="$HOME/.local/share/icons/penguin.png"
BIN_DIR="$HOME/.local/bin"

rm -f "$DESKTOP_FILE"
rm -f "$ICON_FILE"
rm -f "$BIN_DIR/penguinweather-install"
rm -f "$BIN_DIR/penguinweather-uninstall"

echo "Uninstall complete."
echo "App files were kept."
echo "To reinstall, go to the repo folder and run:"
echo "./setup.sh"
