"""
theme
=====
Qtile theme configuration with color palette, fonts, and spacing.
"""

from __future__ import annotations

from typing import Final, TypedDict


class Palette(TypedDict):
    """Color palette for Qtile theme."""

    bg: str
    fg: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    bg_alt: str
    fg_alt: str


PALETTE: Final[Palette] = {
    # Tokyo Night inspired dark theme
    "bg": "#1a1b26",  # Dark background
    "bg_alt": "#24283b",  # Slightly lighter background
    "fg": "#c0caf5",  # Light text
    "fg_alt": "#7982a9",  # Muted text
    "red": "#f7768e",  # Bright red
    "green": "#9ece6a",  # Bright green
    "yellow": "#e0af68",  # Warm yellow
    "blue": "#7aa2f7",  # Bright blue
    "magenta": "#bb9af7",  # Purple
    "cyan": "#7dcfff",  # Bright cyan
    "active_border": "#a855f7",  # Brighter purple for active window borders
    # Monitor-specific colors - distinct but unified with theme
    "monitor_1": "#7aa2f7",  # Blue for primary monitor (using existing blue)
    "monitor_2": "#9ece6a",  # Green for secondary monitor (using existing green)
    "monitor_3": "#bb9af7",  # Magenta for tertiary monitor (using existing magenta)
}

# Spacing and sizing
GAP: Final[int] = 8
BORDER_WIDTH: Final[int] = 4  # Increased to 4px for much better visibility
MARGIN: Final[int] = 3

# Typography
FONT: Final[str] = "JetBrainsMono Nerd Font, FiraCode Nerd Font, monospace"
FONTSIZE: Final[int] = 12
FONT_ALT: Final[str] = "FiraCode Nerd Font, monospace"
FONTSIZE_ALT: Final[int] = 14

# Bar configuration
BAR_HEIGHT: Final[int] = 24
BAR_PADDING: Final[int] = 6

# Layout configuration
LAYOUT_THEME: Final[dict[str, int | str]] = {
    "border_width": BORDER_WIDTH,
    "margin": MARGIN,
    "border_focus": PALETTE["active_border"],  # Dark purple for active windows
    "border_normal": "#444444",  # Subtle gray for inactive windows
}
