#!/usr/bin/env bash
set -euo pipefail

# Helpers
have() { command -v "$1" >/dev/null 2>&1; }
run_bg_once() { pgrep -xu "$USER" "$1" >/dev/null 2>&1 || "$@" & }

# 1) Screen layout
xrandr --output DVI-I-2-2 --mode 5120x1440 --pos 1920x0 --primary --output DVI-I-1-1 --mode 2560x1440 --rate 60 --pos 7040x0 --output eDP-1 --mode 1920x1200 --pos 0x0

# 2) Wallpaper (no per-output hardcoding)
WALLPAPER="${WALLPAPER:-$HOME/Pictures/vivek-kumar-JS_ohjocm00-unsplash.jpg}"
if have xwallpaper && [[ -f "$WALLPAPER" ]]; then
  xwallpaper --stretch "$WALLPAPER" || true
fi

# 3) Keyboard layout (Qtile session only; greeter is separate)
have setxkbmap && setxkbmap us || true

# 4) Compositor
have picom && run_bg_once picom

# 5) Tray helpers (optional; pick what you actually use)
have nm-applet && run_bg_once nm-applet nm-applet
have blueman-applet && run_bg_once blueman-applet blueman-applet
have pasystray && run_bg_once pasystray pasystray

# 6) Screenshot tool (flameshot can be annoying; keep optional)
# have flameshot && run_bg_once flameshot flameshot
