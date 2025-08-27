"""Qtile hooks for startup, events, and error handling."""
from __future__ import annotations

import subprocess

from libqtile import hook

from . import apps
from .utils import ensure_dir, get_qtile_log_path


@hook.subscribe.startup_once
def startup_once() -> None:
    """Run once on Qtile startup - launch daemons and services."""
    # Ensure Qtile log directory exists
    log_path = get_qtile_log_path()
    ensure_dir(log_path.parent)

    # Start eww bar if available (idempotent)
    if apps.EWW:
        try:
            subprocess.Popen(
                ["eww", "daemon"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            # Small delay to let daemon start
            subprocess.Popen(
                ["sleep", "1"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            subprocess.Popen(
                ["eww", "open", "bar"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except (subprocess.SubprocessError, FileNotFoundError):
            pass  # eww not available, continue

    # Start other services (non-blocking)
    services = [
        ["picom", "--experimental-backends"],  # Compositor
        ["nm-applet"],  # Network manager
        ["blueman-applet"],  # Bluetooth manager
        ["pasystray"],  # PulseAudio system tray
    ]

    for service in services:
        try:
            subprocess.Popen(
                service,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except (subprocess.SubprocessError, FileNotFoundError):
            pass  # Service not available, continue


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
