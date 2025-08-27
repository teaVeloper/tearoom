"""
keys.py
"""

import os

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

HOME = os.path.expanduser("~")
VOL = f"{HOME}/.config/qtile/scripts/volume.sh"

mod = "mod4"  # Super key
alt_mod = "mod1"
terminal = "kitty"


def shrink_column(direction):
    def _shrink(qtile):
        layout = qtile.current_layout
        if direction == "left":
            layout.previous()
            layout.grow_right()
            layout.next()
        elif direction == "right":
            layout.next()
            layout.grow_left()
            layout.previous()

    return lazy.function(_shrink)


default_keys = [
    # Navigation like vim/tmux
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down (stack)"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up (stack)"),
    # Swap panes
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Resize panes
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control", "shift"], "h", shrink_column("left")),
    Key([mod, "control", "shift"], "l", shrink_column("right")),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset sizes"),
    # Launch terminal / rofi
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Close window"),
    Key([mod], "r", lazy.spawn("rofi -show run")),
    Key([mod], "w", lazy.spawn("rofi -show window")),
    # Screenshots & lock
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Screenshot"),
    Key([mod, "shift"], "z", lazy.spawn("i3lock")),
    # Restart/Quit
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset column sizes"),
    Key(
        [mod],
        "t",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Toggle scratchpad terminal",
    ),
]


media_keys = [
    # Media: volume via our script
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn(f"{VOL} up"),
        desc="Volume up",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn(f"{VOL} down"),
        desc="Volume down",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn(f"{VOL} mute"),
        desc="Toggle mute",
    ),
    # Media transport (playerctl)
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next track"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous track"),
    # Brightness
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="Brightness up",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="Brightness down",
    ),
]

keys = default_keys + media_keys

mouse = [
    # Tiled window resizing
    # Drag([mod], "Button3", lazy.window.set_size(), start=lazy.window.get_size()),
    Drag([mod], "Button3", lazy.layout.grow_right(), start=lazy.window.get_position()),
    # Optional: tiled window moving
    Drag(
        [mod], "Button1", lazy.window.set_position(), start=lazy.window.get_position()
    ),
    # Floating window support (Alt modifier)
    Drag(
        [alt_mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [alt_mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([alt_mod], "Button2", lazy.window.bring_to_front()),
]
