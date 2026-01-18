"""
screens
=======
Screen configurations for Qtile - bars and panels per monitor.
"""

from __future__ import annotations

from libqtile import bar, widget
from libqtile.config import Screen

from .theme import BAR_HEIGHT, PALETTE
from .widgets import (
    create_battery,
    create_clock,
    create_group_box,
    create_systray,
    create_volume,
    create_window_name,
)


def create_primary_bar() -> bar.Bar:
    """Create primary bar with full widget set."""
    widgets = [
        create_group_box(),
        widget.Prompt(),
        create_window_name(),
        widget.Chord(),
        widget.CurrentLayout(),
        widget.CurrentScreen(),
        widget.Spacer(),
        create_volume(),
        create_battery(),
        create_clock(),
        create_systray(),
    ]

    return bar.Bar(
        widgets,
        BAR_HEIGHT,
        background=PALETTE["bg"],
        opacity=0.95,
    )


def create_secondary_bar() -> bar.Bar:
    """Create secondary bar without systray."""
    widgets = [
        create_group_box(),
        widget.Prompt(),
        create_window_name(),
        widget.Chord(),
        widget.CurrentLayout(),
        widget.CurrentScreen(),
        widget.Spacer(),
        create_volume(),
        create_battery(),
        create_clock(),
    ]

    return bar.Bar(
        widgets,
        BAR_HEIGHT,
        background=PALETTE["bg"],
        opacity=0.95,
    )


def create_minimal_bar() -> bar.Bar:
    """Create minimal bar for smaller screens (same widgets as secondary)."""
    widgets = [
        create_group_box(),
        widget.Prompt(),
        create_window_name(),
        widget.Chord(),
        widget.CurrentLayout(),
        widget.Spacer(),
        create_volume(),
        create_battery(),
        create_clock(),
    ]

    return bar.Bar(
        widgets,
        BAR_HEIGHT,
        background=PALETTE["bg"],
        opacity=0.95,
    )


# Screen configurations
screens: list[Screen] = [
    # Primary screen (ultrawide) - full bar
    Screen(
        top=create_primary_bar(),
        bottom=None,
        left=None,
        right=None,
    ),
    # Secondary screen - standard bar
    Screen(
        top=create_secondary_bar(),
        bottom=None,
        left=None,
        right=None,
    ),
    # Tertiary screen - minimal bar
    Screen(
        top=create_minimal_bar(),
        bottom=None,
        left=None,
        right=None,
    ),
]
