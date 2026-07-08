"""
hooks
=====
Qtile hooks for startup, events, and error handling.
"""

from __future__ import annotations

import logging
import os
import subprocess

from libqtile import hook

from .display import apply_profile, infer_and_apply, trandr_env
from .paths import compute_paths
from .settings import load_cfg

LOG = logging.getLogger(__name__)


def _display_env(cfg: object) -> dict[str, str]:
    env = trandr_env()
    startup_profile = getattr(cfg, "startup_profile", None)
    if startup_profile:
        env["TRANDR_STARTUP_PROFILE"] = startup_profile
    startup_laptop_position = getattr(cfg, "startup_laptop_position", None)
    if startup_laptop_position:
        env["TRANDR_INFER_LAPTOP_POSITION"] = startup_laptop_position
    env["TRANDR_PRIMARY"] = getattr(cfg, "primary", "laptop")
    return env


@hook.subscribe.startup_once
def startup_once() -> None:
    """Run once on startup."""
    paths = compute_paths()
    cfg = load_cfg(paths)
    autostart_script = cfg.core.autostart_script or paths.autostart_script_default

    if os.path.exists(autostart_script):
        subprocess.run([str(autostart_script)], check=False, env=_display_env(cfg.trandr))
    else:
        # Fallback to individual commands if script doesn't exist
        subprocess.run(["eww", "daemon"], check=False)
        subprocess.run(["picom"], check=False)
        subprocess.run(["nm-applet"], check=False)
        subprocess.run(["blueman-applet"], check=False)
        subprocess.run(["pasystray"], check=False)

        if cfg.trandr.startup_profile:
            apply_profile(cfg.trandr.startup_profile, check=False)
        elif cfg.trandr.startup_laptop_position:
            infer_and_apply(
                cfg.trandr.startup_laptop_position,
                primary=cfg.trandr.primary,
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
    paths = compute_paths()
    cfg = load_cfg(paths)
    if not cfg.trandr.screen_change_profile:
        return
    try:
        apply_profile(cfg.trandr.screen_change_profile, check=False)
    except Exception as exc:  # pragma: no cover - Qtile runtime path
        LOG.warning("failed to reapply trandr profile on screen change: %s", exc)
