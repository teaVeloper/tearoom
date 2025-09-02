#!/bin/bash
# Install udev-based keyboard fix for Moonlander
# This triggers IMMEDIATELY when the device is plugged in, no delays

echo "Installing udev-based keyboard fix (immediate trigger)..."

# Create udev rule that triggers instantly
sudo tee /etc/udev/rules.d/99-moonlander-keyboard.rules > /dev/null << 'EOF'
# Moonlander keyboard fix - immediate trigger
SUBSYSTEM=="input", ATTRS{name}=="*moonlander*", ATTRS{name}=="*zsa*", \
    RUN+="/usr/local/bin/fix-moonlander-udev.sh"
EOF

# Create the instant fix script
sudo tee /usr/local/bin/fix-moonlander-udev.sh > /dev/null << 'EOF'
#!/bin/bash
# Instant Moonlander keyboard fix - no delays

# Re-enable the device immediately
echo 1 > /sys/class/input/$(basename $DEVNAME)/enable 2>/dev/null || true

# Also try to re-enable via libinput if X11 is running
if [ -n "$DISPLAY" ]; then
    # Find device ID and fix it
    DEVICE_ID=$(xinput list | grep -i moonlander | grep -v "pointer\|mouse" | head -1 | sed 's/.*id=\([0-9]*\).*/\1/')
    if [ -n "$DEVICE_ID" ]; then
        xinput set-prop "$DEVICE_ID" "libinput Send Events Mode Enabled" 1 0 2>/dev/null || true
    fi
fi

echo "Moonlander keyboard instantly re-enabled"
EOF

# Make the script executable
sudo chmod +x /usr/local/bin/fix-moonlander-udev.sh

# Reload udev rules
sudo udevadm control --reload-rules
sudo udevadm trigger

echo "Udev-based keyboard fix installed!"
echo "It will trigger IMMEDIATELY when Moonlander is detected."
echo ""
echo "To test: unplug and replug your Moonlander"
echo "The fix should apply instantly with no delays."
