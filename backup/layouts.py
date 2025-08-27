"""
layouts.py
"""

from libqtile import layout

# Layouts
layout_theme = {
    "border_width": 1,
    "margin": 3,
    "border_focus": "#a151d3",
    "border_normal": "#444444",
}

col_layout = {
    **layout_theme,
    "num_columns": 3,
    "insert_position": 1,  # middle by default
    "wrap_focus_columns": False,
}


layouts = [
    layout.Columns(**col_layout),  # Perfect for tiling on ultrawide
    # layout.MonadTall(**layout_theme),
    layout.MonadThreeCol(**layout_theme, ratio=0.4),
    # layout.Stack(**layout_theme),
    layout.Max(),
]
