"""Essential Qtile widgets - minimal set for basic functionality."""
from __future__ import annotations

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
    """Create styled group box widget."""
    return widget.GroupBox(
        active=PALETTE["fg"],
        inactive=PALETTE["fg_alt"],
        block_highlight_text_color=PALETTE["bg"],
        highlight_color=PALETTE["magenta"],
        urgent_alert_method="border",
        urgent_border=PALETTE["red"],
        other_current_screen_border=PALETTE["yellow"],
        other_screen_border=PALETTE["green"],
        # Make groups clearly visible and clickable
        borderwidth=4,
        padding=8,
        spacing=4,
        # Show group names clearly
        fontsize=14,
        # Make sure groups are visible even when empty
        hide_unused=False,
        # Add some spacing between groups
        margin_x=4,
        # Make current group more prominent
        this_current_screen_border=PALETTE["magenta"],
        this_screen_border=PALETTE["blue"],
        # Use rounded corners for modern look
        rounded=True,
        # Force visibility and make it obvious
        visible_groups=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        # Use block highlighting for maximum visibility
        highlight_method="block",
        # Ensure text is always visible
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


def create_volume() -> widget.Volume:
    """Create styled volume widget."""
    return widget.Volume(
        fmt=" {}",
        emoji=True,
        emoji_list=["🔇", "🔈", "🔉", "🔊"],
        volume_app="pavucontrol",
    )
