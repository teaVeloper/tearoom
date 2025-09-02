#!/bin/bash
# Diagnostic script to check input devices and their properties

echo "=== INPUT DEVICE DIAGNOSTICS ==="
echo

echo "All input devices:"
xinput list
echo

echo "Moonlander devices specifically:"
xinput list | grep -i moonlander
echo

echo "Device 21 (keyboard) properties:"
xinput list-props 21 | grep -E "(Device|libinput|Enabled)"
echo

echo "Device 10 (pointer) properties:"
xinput list-props 10 | grep -E "(Device|libinput|Enabled)"
echo

echo "Device 11 (mouse) properties:"
xinput list-props 11 | grep -E "(Device|libinput|Enabled)"
echo

