#!/bin/bash

sinks=$(pactl list short sinks | awk '{print $2}')
chosen=$(echo "$sinks" | rofi -dmenu -i -p "Audio Sink")

if [[ -n "$chosen" ]]; then
  pactl set-default-sink "$chosen"
fi

