"""
apps
====
Application commands and launchers for Qtile configuration.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

# SET HOME
HOME = str(Path.home())

# Terminal and editor
KITTY: Final[list[str]] = ["kitty"]
EDITOR: Final[list[str]] = KITTY + ["-e", "nvim"]
EDITOR_ALT: Final[list[str]] = ["nvim"]

# Launchers
LAUNCHER: Final[list[str]] = ["rofi", "-show", "drun"]
RUNNER: Final[list[str]] = ["rofi", "-show", "run"]
WINDOW_SWITCHER: Final[list[str]] = ["rofi", "-show", "window"]

# Browser and file manager
BROWSER: Final[list[str]] = ["firefox"]  # launch firefox directly
FILE_MANAGER: Final[list[str]] = ["xdg-open", "."]

# System tools
EWW: Final[list[str]] = ["eww"]
SCREENSHOT: Final[list[str]] = ["flameshot", "gui"]
LOCK: Final[list[str]] = ["i3lock"]

# Power management (no confirmation needed for these key combinations)
SUSPEND: Final[list[str]] = ["systemctl", "suspend"]
SHUTDOWN: Final[list[str]] = ["systemctl", "poweroff"]
REBOOT: Final[list[str]] = ["systemctl", "reboot"]
LOGOUT: Final[list[str]] = ["qtile", "cmd-obj", "-o", "cmd", "-f", "shutdown"]

# Media controls - using your reliable volume script

VOLUME_UP = [f"{HOME}/.config/qtile/scripts/volume.sh", "up"]
VOLUME_DOWN = [f"{HOME}/.config/qtile/scripts/volume.sh", "down"]
VOLUME_MUTE = [f"{HOME}/.config/qtile/scripts/volume.sh", "mute"]
BRIGHTNESS_UP: Final[list[str]] = ["brightnessctl", "set", "+5%"]
BRIGHTNESS_DOWN: Final[list[str]] = ["brightnessctl", "set", "5%-"]

# Player controls
PLAYER_PLAY: Final[list[str]] = ["playerctl", "play-pause"]
PLAYER_NEXT: Final[list[str]] = ["playerctl", "next"]
PLAYER_PREV: Final[list[str]] = ["playerctl", "previous"]
