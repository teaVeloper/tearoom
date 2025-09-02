"""Comprehensive keybindings for Qtile configuration - SUPER-based navigation."""
from __future__ import annotations

from libqtile.config import Key, Mouse
from libqtile.lazy import lazy

from . import apps
from .constants import mod

# Core application launchers
app_launchers: list[Key] = [
    Key([mod], "Return", lazy.spawn(apps.KITTY), desc="Launch kitty terminal"),
    Key([mod], "space", lazy.spawn(apps.LAUNCHER), desc="Launch rofi drun"),
    Key([mod], "b", lazy.spawn(apps.BROWSER), desc="Launch Firefox directly"),
    Key([mod], "f", lazy.spawn(apps.FILE_MANAGER), desc="Open file manager"),
    Key(
        [mod],
        "BackSpace",
        lazy.spawn(apps.WINDOW_SWITCHER),
        desc="Launch rofi window switcher",
    ),
    # Test key to verify Qtile is receiving key events
    Key([mod], "v", lazy.spawn("notify-send 'TEST' 'Super+V works!' -t 2000"), desc="Test key"),
]

# System actions
system_actions: list[Key] = [
    Key([mod], "q", lazy.window.kill(), desc="Close window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload Qtile config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "z", lazy.spawn(apps.LOCK), desc="Lock screen"),
    Key([mod, "shift"], "s", lazy.spawn(apps.SCREENSHOT), desc="Take screenshot"),
]

# Power management (hard to press accidentally - no confirmation needed)
power_actions: list[Key] = [
    Key([mod, "mod1", "control"], "Escape", lazy.spawn(apps.SUSPEND), desc="Suspend system"),
    Key([mod, "mod1", "control"], "Return", lazy.spawn(apps.SHUTDOWN), desc="Shutdown system"),
    Key([mod, "mod1", "control"], "r", lazy.spawn(apps.REBOOT), desc="Reboot system"),
    Key([mod, "mod1", "control"], "l", lazy.spawn(apps.LOGOUT), desc="Logout Qtile"),
    # Power menu for more options
    Key([mod, "mod1", "control"], "p", lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu"), desc="Power menu"),
]

# Navigation keys (vim-style with arrow fallbacks)
navigation_keys: list[Key] = [
    # Focus navigation
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right"),
    # Arrow key alternatives
    Key([mod], "Left", lazy.layout.left(), desc="Move focus left (arrow)"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down (arrow)"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up (arrow)"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus right (arrow)"),
]

# Window management
window_management: list[Key] = [
    # Window movement
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    # Layout control
    Key([mod], "Tab", lazy.next_layout(), desc="Next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Previous layout"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset column sizes"),
    # Awesome rofi layout switcher
    Key([mod, "shift"], "g", lazy.spawn("~/.config/qtile/bin/layout_switcher.py"), desc="Rofi layout switcher"),
]

# Window resizing (your working setup)
window_resize: list[Key] = [
    # Resize operations (Super+Ctrl+h/j/k/l)
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow left"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow up"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow right"),
    # Column shrinking (Super+Ctrl+Shift+h/l)
    Key([mod, "control", "shift"], "h", lazy.layout.grow_left(), desc="Shrink left"),
    Key([mod, "control", "shift"], "l", lazy.layout.grow_right(), desc="Shrink right"),
]

# Media and system controls with visual feedback
media_controls: list[Key] = [
    # Volume control with notifications
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("/home/bertold/.config/qtile/scripts/volume.sh up && notify-send 'Volume' 'Volume increased' -t 1000"),
        desc="Volume up",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("/home/bertold/.config/qtile/scripts/volume.sh down && notify-send 'Volume' 'Volume decreased' -t 1000"),
        desc="Volume down",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("/home/bertold/.config/qtile/scripts/volume.sh mute && notify-send 'Volume' 'Volume muted' -t 1000"),
        desc="Toggle mute",
    ),
    # Media transport
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause && notify-send 'Media' 'Play/Pause' -t 1000"),
        desc="Play/Pause",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl next && notify-send 'Media' 'Next track' -t 1000"),
        desc="Next track",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous && notify-send 'Media' 'Previous track' -t 1000"),
        desc="Previous track",
    ),
    # Brightness with notifications
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5% && notify-send 'Brightness' 'Brightness increased' -t 1000"),
        desc="Brightness up",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%- && notify-send 'Brightness' 'Brightness decreased' -t 1000"),
        desc="Brightness down",
    ),
    # Screenshot
    Key([], "Print", lazy.spawn(apps.SCREENSHOT), desc="Screenshot"),
]

# Mouse bindings
mouse: list[Mouse] = [
    # Tiled window resizing
    Mouse([mod], "Button3", lazy.layout.grow_right()),
    # Optional: tiled window moving
    Mouse([mod], "Button1", lazy.window.set_position()),
    # Floating window support (Alt modifier)
    Mouse(["mod1"], "Button1", lazy.window.set_position_floating()),
    Mouse(["mod1"], "Button3", lazy.window.set_size_floating()),
    Mouse(["mod1"], "Button2", lazy.window.bring_to_front()),
]

# Merge all keybinding groups (without group keys for now)
keys: list[Key] = (
    app_launchers
    + system_actions
    + power_actions
    + navigation_keys
    + window_management
    + window_resize
    + media_controls
)
