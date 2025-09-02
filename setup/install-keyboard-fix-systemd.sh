#!/bin/bash
# Install system-level keyboard fix for Moonlander
# This runs BEFORE the login manager, fixing the keyboard at boot

echo "Installing system-level keyboard fix..."

# Create the systemd service file
sudo tee /etc/systemd/system/moonlander-keyboard-fix.service > /dev/null << 'EOF'
[Unit]
Description=Fix Moonlander keyboard at boot
Before=display-manager.service
After=systemd-user-sessions.service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/fix-moonlander-keyboard.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

# Create the actual fix script
sudo tee /usr/local/bin/fix-moonlander-keyboard.sh > /dev/null << 'EOF'
#!/bin/bash
# System-level fix for Moonlander keyboard - fast version

# Minimal wait for input subsystem to be ready
sleep 1

# Find and fix Moonlander keyboard immediately
MOONLANDER_DEVICE=$(find /sys/class/input/ -name "*moonlander*" -o -name "*zsa*" | head -1)
if [ -n "$MOONLANDER_DEVICE" ]; then
    echo "Found Moonlander device: $MOONLANDER_DEVICE"
    # Re-enable the device instantly
    echo 1 > "$MOONLANDER_DEVICE/enable" 2>/dev/null || true
fi

# Trigger udev to re-scan input devices (fast)
udevadm trigger --subsystem-match=input --action=add

echo "Moonlander keyboard fix applied (fast mode)"
EOF

# Make the script executable
sudo chmod +x /usr/local/bin/fix-moonlander-keyboard.sh

# Enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable moonlander-keyboard-fix.service

echo "System-level keyboard fix installed and enabled."
echo "It will run automatically at every boot (fast mode)."
echo ""
echo "To test immediately: sudo systemctl start moonlander-keyboard-fix.service"
echo "To check status: sudo systemctl status moonlander-keyboard-fix.service"
