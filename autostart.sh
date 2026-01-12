#!/usr/bin/env bash
set -euo pipefail

# Helpers
have() { command -v "$1" >/dev/null 2>&1; }
run_bg_once() { pgrep -xu "$USER" "$1" >/dev/null 2>&1 || "$@" & }

# 1) Screen layout
if have autorandr; then
  # Use autorandr profiles if available (best for office/home switching)
  autorandr --change --force || true
else
  # Fallback: just enable what’s connected
  have xrandr && xrandr --auto || true
fi

# 2) Wallpaper (no per-output hardcoding)
WALLPAPER="${WALLPAPER:-$HOME/Pictures/vivek-kumar-JS_ohjocm00-unsplash.jpg}"
if have xwallpaper && [[ -f "$WALLPAPER" ]]; then
  xwallpaper --stretch "$WALLPAPER" || true
fi

# 3) Keyboard layout (Qtile session only; greeter is separate)
have setxkbmap && setxkbmap us || true

# 4) Compositor
have picom && run_bg_once picom picom

# 5) Tray helpers (optional; pick what you actually use)
have nm-applet && run_bg_once nm-applet nm-applet
have blueman-applet && run_bg_once blueman-applet blueman-applet
have pasystray && run_bg_once pasystray pasystray

# 6) Screenshot tool (flameshot can be annoying; keep optional)
# have flameshot && run_bg_once flameshot flameshot
