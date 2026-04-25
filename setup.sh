#!/bin/bash

echo "Install Penguin Weather"
read -p "Continue? (y/n): " confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Install cancelled."
    exit 0
fi

APP_FOLDER="$HOME/rpi-penguinweather-app"
DESKTOP_FILE="$HOME/.local/share/applications/penguinweather.desktop"
ICON_DIR="$HOME/.local/share/icons"
ICON_FILE="$ICON_DIR/penguin.png"
BIN_DIR="$HOME/.local/bin"

echo "Installing dependencies..."
sudo apt update
sudo apt install -y python3-venv python3-tk fonts-noto-color-emoji

cd "$APP_FOLDER" || {
    echo "Error: Could not find $APP_FOLDER"
    exit 1
}

echo "Setting up Python environment..."
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

echo "Creating universal commands..."
mkdir -p "$BIN_DIR"

cat > "$BIN_DIR/penguinweather-install" <<EOF
#!/bin/bash
cd "$APP_FOLDER"
./setup.sh
EOF

cat > "$BIN_DIR/penguinweather-uninstall" <<EOF
#!/bin/bash
cd "$APP_FOLDER"
./uninstall.sh
EOF

chmod +x "$BIN_DIR/penguinweather-install"
chmod +x "$BIN_DIR/penguinweather-uninstall"

echo "Install complete."
echo "You can now run:"
echo "penguinweather-install"
echo "penguinweather-uninstall"
echo ""
echo "If the commands do not work, restart your terminal or reboot."
