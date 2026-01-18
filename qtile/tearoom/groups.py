"""
groups
======
Group configurations for Qtile - workspace organization.
"""

from __future__ import annotations

from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.lazy import lazy

from .constants import mod

# Workspace groups with labels and default layouts
groups: list[Group] = [
    Group(
        "1",
        label="1",
        layout="monadthreecol",
        spawn=["kitty"],
    ),
    Group(
        "2",
        label="2",
        layout="max",
        spawn=["firefox"],
    ),
    Group(
        "3",
        label="3",
        layout="max",
        spawn=["thunderbird"],
    ),
    Group(
        "4",
        label="4",
        layout="columns",
        spawn=["kitty"],
    ),
    Group(
        "5",
        label="5",
        layout="monadthreecol",
        spawn=["discord"],
    ),
    Group(
        "6",
        label="6",
        layout="columns",
        spawn=["kitty"],
    ),
    Group(
        "7",
        label="7",
        layout="columns",
        spawn=["kitty"],
    ),
    Group(
        "8",
        label="8",
        layout="columns",
        spawn=["kitty"],
    ),
    Group(
        "9",
        label="9",
        spawn=["kitty"],
    ),
]

# Scratchpad for quick access tools
scratchpad = ScratchPad(
    "scratchpad",
    [
        DropDown(
            "term",
            "kitty --class=scratchpad",
            width=0.6,
            height=0.5,
            x=0.2,
            y=0.1,
            opacity=0.95,
            on_focus_lost_hide=True,
        ),
        DropDown(
            "ranger",
            "kitty --class=scratchpad -e ranger",
            width=0.6,
            height=0.6,
            x=0.2,
            y=0.1,
            opacity=0.95,
            on_focus_lost_hide=True,
        ),
        DropDown(
            "htop",
            "kitty --class=scratchpad -e htop",
            width=0.7,
            height=0.7,
            x=0.15,
            y=0.15,
            opacity=0.95,
            on_focus_lost_hide=True,
        ),
    ],
)

# Add scratchpad to groups
groups.append(scratchpad)

# Generate group keybindings
group_keys: list[Key] = []

for group in groups:
    if group.name != "scratchpad":
        group_keys.extend(
            [
                # Switch to group
                Key(
                    [mod],
                    group.name,
                    lazy.group[group.name].toscreen(),
                    desc=f"Switch to group {group.name}",
                ),
                # Move window to group
                Key(
                    [mod, "shift"],
                    group.name,
                    lazy.window.togroup(group.name),
                    desc=f"Move window to group {group.name}",
                ),
            ]
        )

# Scratchpad keybindings
group_keys.extend(
    [
        Key(
            [mod],
            "t",
            lazy.group["scratchpad"].dropdown_toggle("term"),
            desc="Toggle scratchpad terminal",
        ),
        Key(
            [mod, "shift"],
            "r",
            lazy.group["scratchpad"].dropdown_toggle("ranger"),
            desc="Toggle scratchpad file manager",
        ),
        Key(
            [mod, "shift"],
            "i",  # Changed from 'h' to avoid conflict with move window left
            lazy.group["scratchpad"].dropdown_toggle("htop"),
            desc="Toggle scratchpad system monitor",
        ),
    ]
)

# Note: group_keybindings will be populated by the keys module
# This avoids circular imports while maintaining the organized structure
