"""
paths
=====
define default paths for config and data storage and define data structures for internal usage
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _xdg_dir(env_key: str, default_suffix: str) -> Path:
    v = os.environ.get(env_key)
    if v:
        return Path(v)
    return Path.home() / default_suffix


def xdg_config_home() -> Path:
    return _xdg_dir("XDG_CONFIG_HOME", ".config")


def xdg_state_home() -> Path:
    return _xdg_dir("XDG_STATE_HOME", ".local/state")


def xdg_cache_home() -> Path:
    return _xdg_dir("XDG_CACHE_HOME", ".cache")


@dataclass(frozen=True)
class TearoomPaths:
    # Repo (inside ~/.config/qtile)
    qtile_dir: Path
    defaults_dir: Path
    default_toml: Path
    default_display_profiles_dir: Path

    autostart_script_default: Path
    repo_default_wallpaper: Path
    state_wallpaper_link: Path

    # User
    user_toml_primary: Path
    user_toml_fallback: Path

    # Runtime
    state_dir: Path
    state_display_dir: Path
    state_last_json: Path

    cache_dir: Path


def compute_paths() -> TearoomPaths:
    # tearoom package dir: ~/.config/qtile/tearoom
    pkg_dir = Path(__file__).resolve().parent
    qtile_dir = pkg_dir.parent  # ~/.config/qtile

    defaults_dir = qtile_dir / "defaults"
    default_toml = defaults_dir / "config.toml"
    default_display_profiles_dir = defaults_dir / "display-profiles"

    autostart_script_default = qtile_dir / "scripts" / "autostart.sh"
    repo_default_wallpaper = qtile_dir / "assets" / "wallpaper.jpg"

    cfg_home = xdg_config_home()
    user_toml_primary = cfg_home / "teagarden" / "tearoom" / "config.toml"
    user_toml_fallback = cfg_home / "teagarden" / "tearoom.toml"

    state_dir = xdg_state_home() / "tearoom" / "qtile"
    state_display_dir = state_dir / "display"
    state_last_json = state_dir / "last.json"
    state_wallpaper_link = state_dir / "wallpaper"

    cache_dir = xdg_cache_home() / "tearoom" / "qtile"

    return TearoomPaths(
        qtile_dir=qtile_dir,
        defaults_dir=defaults_dir,
        default_toml=default_toml,
        default_display_profiles_dir=default_display_profiles_dir,
        autostart_script_default=autostart_script_default,
        repo_default_wallpaper=repo_default_wallpaper,
        state_wallpaper_link=state_wallpaper_link,
        user_toml_primary=user_toml_primary,
        user_toml_fallback=user_toml_fallback,
        state_dir=state_dir,
        state_display_dir=state_display_dir,
        state_last_json=state_last_json,
        cache_dir=cache_dir,
    )
