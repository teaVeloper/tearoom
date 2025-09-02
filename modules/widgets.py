"""Essential Qtile widgets - minimal set for basic functionality."""
from __future__ import annotations

import subprocess

from libqtile import widget

from .theme import BAR_PADDING, FONT, FONTSIZE, PALETTE

# Widget defaults
widget_defaults = dict(
    font=FONT,
    fontsize=FONTSIZE,
    padding=BAR_PADDING,
    background=PALETTE["bg"],
    foreground=PALETTE["fg"],
)

extension_defaults = widget_defaults.copy()


def create_group_box() -> widget.GroupBox:
    """Create group box widget with nice, subtle colors."""
    return widget.GroupBox(
        # Nice, subtle colors
        active=PALETTE["fg"],           # Active groups in main text color
        inactive=PALETTE["fg_alt"],     # Inactive groups in muted text color
        block_highlight_text_color=PALETTE["bg"],
        highlight_color=PALETTE["magenta"],
        urgent_alert_method="border",
        urgent_border=PALETTE["red"],
        
        # Subtle monitor colors - these only show current vs other screens
        this_current_screen_border=PALETTE["monitor_1"],      # Current monitor groups
        this_screen_border=PALETTE["monitor_1"],              # Current monitor groups
        other_current_screen_border=PALETTE["monitor_2"],     # Other monitor active groups
        other_screen_border=PALETTE["monitor_3"],             # Other monitor inactive groups
        
        # Visual styling
        borderwidth=3,
        padding=6,
        spacing=3,
        fontsize=13,
        hide_unused=False,
        margin_x=3,
        rounded=True,
        visible_groups=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        highlight_method="block",
    )


def create_clock() -> widget.Clock:
    """Create styled clock widget."""
    return widget.Clock(
        format="%Y-%m-%d %H:%M",
        mouse_callbacks={"Button1": lambda: None},  # TODO: Add calendar popup
    )


def create_window_name() -> widget.WindowName:
    """Create styled window name widget."""
    return widget.WindowName(
        max_chars=60,
        empty_group_string="Desktop",
    )


def create_systray() -> widget.Systray:
    """Create styled system tray widget."""
    return widget.Systray(
        icon_size=16,
        padding=4,
    )


def create_battery() -> widget.Battery:
    """Create styled battery widget."""
    return widget.Battery(
        format="{char} {percent:2.0%}",
        charge_char="",
        discharge_char="",
        full_char="",
        unknown_char="",
        empty_char="",
        low_percentage=0.15,
        low_foreground=PALETTE["red"],
        show_short_text=False,
    )


def create_volume() -> widget.GenPollText:
    """Create custom mute status indicator using same method as volume script."""
    return widget.GenPollText(
        func=lambda: "🔇" if "yes" in subprocess.run(
            ["pactl", "get-sink-mute", "@DEFAULT_SINK@"], 
            capture_output=True, text=True
        ).stdout else "🔊",
        update_interval=0.5,  # Update every 0.5 seconds (more responsive)
        fmt="{}",
        mouse_callbacks={"Button1": lambda: None},  # No click functionality
    )
