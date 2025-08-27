"""
config. py
"""

# Qtile starter config for ultrawide + multiple monitor + vim-like nav
# Location: ~/.config/qtile/config.py

import os
import subprocess

from groups import groups
from keys import keys, mod, mouse, terminal
from layouts import layouts
from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy


# Autostart script
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])
    # autostart_apps = [
    #     ("firefox", "1"),
    #     ("spotify", "2"),
    #     ("thunderbird", "3"),
    # ]
    #
    # for cmd, group in autostart_apps:
    #     qtile.cmd_spawn(f"{cmd} --class={cmd}")


# Bar and widgets
widget_defaults = dict(font="FiraCode Nerd Font", fontsize=14, padding=6)
extension_defaults = widget_defaults.copy()


def menu_bar(primary: bool = False):
    bar_items = [
        widget.GroupBox(),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(),
        widget.CurrentScreen(),
        widget.CurrentLayout(),
        # widget.PulseVolume(),  # scroll to change, click to mute
        widget.Clock(
            format="%Y-%m-%d %H:%M",
            mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
        ),
        widget.Battery(),
        widget.Bluetooth(),
        widget.Volume(),
    ]
    primary_bar_items = [
        widget.Systray(),
    ]
    if primary:
        items = bar_items + primary_bar_items
    else:
        items = bar_items
    return bar.Bar(
        items,
        24,
    )


screens = [
    Screen(top=menu_bar(primary=True)),  # ultrawide (with bar)
    Screen(top=menu_bar()),  # e.g. laptop (no bar)
    Screen(top=menu_bar()),  # 2560x1440 (no bar)
]


# Floating rules
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)


# Other config
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "Qtile"
