#!/bin/bash
devices=$(bluetoothctl devices | awk '{$1=$2=""; print substr($0,3)}')
chosen=$(echo "$devices" | rofi -dmenu -p "BT Devices")

mac=$(bluetoothctl devices | grep "$chosen" | awk '{print $2}')
bluetoothctl connect "$mac"

