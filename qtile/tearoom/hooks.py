"""
hooks
=====
Qtile hooks for startup, events, and error handling.
"""

from __future__ import annotations

import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def startup_once() -> None:
    """Run once on startup."""
    # Run the main autostart script
    autostart_script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    if os.path.exists(autostart_script):
        subprocess.run([autostart_script], check=False)
    else:
        # Fallback to individual commands if script doesn't exist
        subprocess.run(["eww", "daemon"], check=False)
        subprocess.run(["picom"], check=False)
        subprocess.run(["nm-applet"], check=False)
        subprocess.run(["blueman-applet"], check=False)
        subprocess.run(["pasystray"], check=False)

        # Basic screen setup (simple, working version)
        subprocess.run(
            ["xrandr", "--output", "DP-1", "--primary", "--mode", "2560x1440"],
            check=False,
        )
        subprocess.run(
            [
                "xrandr",
                "--output",
                "HDMI-A-0",
                "--mode",
                "1920x1080",
                "--right-of",
                "DP-1",
            ],
            check=False,
        )

        # Set wallpaper (simple, working version)
        wallpaper_path = os.path.expanduser("~/.config/qtile/wallpaper.jpg")
        if os.path.exists(wallpaper_path):
            subprocess.run(
                ["xwallpaper", "--output", "DP-1", "--stretch", wallpaper_path],
                check=False,
            )
            subprocess.run(
                ["xwallpaper", "--output", "HDMI-A-0", "--stretch", wallpaper_path],
                check=False,
            )

        # Set keyboard layout
        subprocess.run(["setxkbmap", "us"], check=False)


@hook.subscribe.startup
def startup() -> None:
    """Run on every Qtile startup."""
    pass


@hook.subscribe.shutdown
def shutdown() -> None:
    """Run on Qtile shutdown."""
    pass


@hook.subscribe.client_new
def client_new(client: object) -> None:
    """Handle new client windows."""
    # Set default floating for certain applications
    floating_classes = [
        "confirmreset",
        "makebranch",
        "maketag",
        "ssh-askpass",
        "pinentry",
        "mpv",
        "vlc",
        "spotify",
    ]

    if client.window.get_wm_class()[0] in floating_classes:
        client.floating = True


@hook.subscribe.client_focus
def client_focus(client: object, window: object) -> None:
    """Handle client focus changes."""
    pass


@hook.subscribe.screen_change
def screen_change() -> None:
    """Handle screen configuration changes."""
    pass
