"""
layouts
=======
Layout configurations for Qtile - sensible defaults with theme integration.
"""

from __future__ import annotations

from libqtile import layout
from libqtile.config import Match
from libqtile.layout.base import Layout

from .theme import LAYOUT_THEME

# Core layouts with consistent theming
layouts: list[Layout] = [
    # Primary tiling layout - perfect for ultrawide monitors
    layout.Columns(
        **LAYOUT_THEME,
        num_columns=3,
        insert_position=1,  # middle by default
        wrap_focus_columns=False,
        follow_mouse_focus=False,  # Disable mouse-following
        name="columns",
    ),
    # Three-column layout with adjustable ratios
    layout.MonadThreeCol(
        **LAYOUT_THEME,
        ratio=0.4,
        change_ratio=0.05,
        follow_mouse_focus=False,  # Disable mouse-following
        name="monadthreecol",
    ),
    # Tall layout for vertical stacking
    layout.MonadTall(
        **LAYOUT_THEME,
        ratio=0.65,
        change_ratio=0.05,
        follow_mouse_focus=False,  # Disable mouse-following
        name="monadtall",
    ),
    # Wide layout for horizontal stacking
    layout.MonadWide(
        **LAYOUT_THEME,
        ratio=0.65,
        change_ratio=0.05,
        follow_mouse_focus=False,  # Disable mouse-following
        name="monadwide",
    ),
    # Stack layout for multiple windows
    layout.Stack(
        **LAYOUT_THEME,
        num_stacks=2,
        follow_mouse_focus=False,  # Disable mouse-following
        name="stack",
    ),
    # Max layout for fullscreen focus
    layout.Max(
        **LAYOUT_THEME,
        follow_mouse_focus=False,  # Disable mouse-following
        name="max",
    ),
    # Tree layout for hierarchical organization
    layout.TreeTab(
        **LAYOUT_THEME,
        active_bg=LAYOUT_THEME["border_focus"],
        active_fg="#ffffff",
        bg_color="#2f2f2f",
        fontsize=10,
        level_shift=8,
        follow_mouse_focus=False,  # Disable mouse-following
        name="treetab",
    ),
]

# Floating layout rules
floating_layout = layout.Floating(
    **LAYOUT_THEME,
    follow_mouse_focus=False,  # Disable mouse-following in floating windows
    float_rules=[
        *layout.Floating.default_float_rules,
        # Application-specific floating rules
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(title="Open File"),
        Match(title="Save File"),
        Match(title="Preferences"),
        Match(title="Settings"),
        # Media players often work better floating
        Match(wm_class="mpv"),
        Match(wm_class="vlc"),
        Match(wm_class="spotify"),
    ],
)
