#!/bin/bash
# System-level fix for Moonlander keyboard being disabled by libinput
# This should run at boot/login, before any desktop environment starts

# Wait for X11 to be ready
sleep 3

# Find Moonlander keyboard specifically (not mouse/pointer)
# Use 'keyboard:' prefix to only target keyboard devices
MOONLANDER_KEYBOARD=$(xinput list | grep -i "moonlander.*keyboard" | head -1 | sed 's/.*id=\([0-9]*\).*/\1/')

if [ -n "$MOONLANDER_KEYBOARD" ]; then
    echo "Found Moonlander keyboard at ID: $MOONLANDER_KEYBOARD"
    xinput set-prop "$MOONLANDER_KEYBOARD" "libinput Send Events Mode Enabled" 1 0
    echo "Keyboard re-enabled"
else
    echo "Moonlander keyboard not found, trying fallback..."
    # Fallback: find any Moonlander device and check if it's keyboard
    MOONLANDER_DEVICES=$(xinput list | grep -i moonlander | grep -v "pointer\|mouse" | head -1 | sed 's/.*id=\([0-9]*\).*/\1/')
    if [ -n "$MOONLANDER_DEVICES" ]; then
        echo "Found Moonlander device at ID: $MOONLANDER_DEVICES"
        xinput set-prop "$MOONLANDER_DEVICES" "libinput Send Events Mode Enabled" 1 0
        echo "Device re-enabled"
    else
        echo "No Moonlander devices found"
    fi
fi

# Set keyboard layout
setxkbmap us

echo "System keyboard fix completed"
