"""Qtile configuration - modular setup with keyboard-driven workflow."""

from __future__ import annotations

from libqtile.config import Key, Match
from libqtile.lazy import lazy

# own modules
from tearoom.constants import mod
from tearoom.groups import group_keys, groups
from tearoom.keys import keys, mouse
from tearoom.layouts import floating_layout, layouts
from tearoom.screens import screens
from tearoom.theme import GAP

# Import hooks so @hook.subscribe handlers are registered.
# This module is imported for its side effects.
from tearoom import hooks  # noqa: F401


# Global configuration
auto_fullscreen = True
focus_on_window_activation = "never"  # Never auto-focus windows on mouse hover
wmname = "Qtile"

# Mouse behavior - ensure no auto-focusing
follow_mouse_focus = False  # Disable mouse-following focus completely

# Gaps and spacing
margin = GAP

# Screen configurations (imported from tearoom/screens.py)
# Qtile requires screens to be defined at module level
screens = screens
layouts = layouts

# Additional floating rules (extend the ones from tearoom/layouts.py)
additional_float_rules = [
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
]

# Extend floating layout with additional rules
floating_layout.float_rules.extend(additional_float_rules)

# Add group keys to the main keys list
keys.extend(group_keys)

# Add error log viewer binding
keys.append(
    Key(
        [mod, "control"],
        "o",  # Changed from 'l' to avoid conflict with grow right
        lazy.spawn("kitty -e nvim ~/.local/share/qtile/qtile.log"),
        desc="View Qtile log in kitty",
    )
)
