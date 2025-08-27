#!/bin/bash

# Set wallpaper
WALLPAPER=~/Pictures/vivek-kumar-JS_ohjocm00-unsplash.jpg
xwallpaper --output DVI-I-1-1 --stretch "$WALLPAPER" \
           --output DVI-I-2-2 --stretch "$WALLPAPER" \
           --output eDP-1     --stretch "$WALLPAPER"
# keyboard
setxkbmap us

# Start compositor for transparency
picom &

# Start flameshot in tray
# flameshot &

# Optional: custom xrandr setup for ultrawide
# Apply monitor layout
xrandr \
  --output DVI-I-1-1 --mode 5120x1440 --pos 1920x0 --primary \
  --output DVI-I-2-2 --mode 2560x1440 --pos 7040x0 \
  --output eDP-1     --mode 1920x1080 --pos 0x147

