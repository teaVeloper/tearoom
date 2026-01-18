"""
settings
========
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .paths import TearoomPaths


@dataclass(frozen=True)
class BarCfg:
    height: int = 24
    opacity: float = 0.95


@dataclass(frozen=True)
class AppsCfg:
    terminal: str = "kitty"
    browser: str = "firefox"
    launcher: str = "rofi -show drun"
    runner: str = "rofi -show run"
    window_switcher: str = "rofi -show window"


@dataclass(frozen=True)
class CoreCfg:
    follow_mouse_focus: bool = False
    wmname: str = "LG3D"
    autostart_script: Path | None = None  # user override only
    use_autorandr: bool = True
    set_wallpaper: bool = True  # allow disabling wallpaper logic


@dataclass(frozen=True)
class TearoomCfg:
    apps: AppsCfg = AppsCfg()
    bar: BarCfg = BarCfg()
    core: CoreCfg = CoreCfg()


def _read_toml(path: Path) -> dict[str, Any]:
    try:
        import tomllib  # py3.11+

        return tomllib.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _deep_get(d: dict[str, Any], key: str, default: Any) -> Any:
    v = d.get(key, default)
    return v


@dataclass(frozen=True)
class EffectivePaths:
    autostart_script: Path
    wallpaper_candidate: Path | None


def compute_effective_paths(paths: TearoomPaths, cfg: CoreCfg) -> EffectivePaths:
    autostart = cfg.autostart_script or paths.autostart_script_default

    wallpaper: Path | None = None
    if cfg.set_wallpaper:
        if paths.state_wallpaper_link.exists():
            wallpaper = paths.state_wallpaper_link
        elif paths.repo_default_wallpaper.exists():
            wallpaper = paths.repo_default_wallpaper

    return EffectivePaths(autostart_script=autostart, wallpaper_candidate=wallpaper)


def load_cfg(paths: TearoomPaths) -> TearoomCfg:
    # layer defaults -> user override
    data: dict[str, Any] = {}

    for p in (paths.default_toml, paths.user_toml_primary, paths.user_toml_fallback):
        if p.exists():
            # shallow merge is enough for v0; later add explicit sections
            data.update(_read_toml(p))

    apps_d = data.get("apps", {}) if isinstance(data.get("apps"), dict) else {}
    bar_d = data.get("bar", {}) if isinstance(data.get("bar"), dict) else {}
    core_d = data.get("core", {}) if isinstance(data.get("core"), dict) else {}

    apps = AppsCfg(
        terminal=str(_deep_get(apps_d, "terminal", AppsCfg.terminal)),
        browser=str(_deep_get(apps_d, "browser", AppsCfg.browser)),
        launcher=str(_deep_get(apps_d, "launcher", AppsCfg.launcher)),
        runner=str(_deep_get(apps_d, "runner", AppsCfg.runner)),
        window_switcher=str(
            _deep_get(apps_d, "window_switcher", AppsCfg.window_switcher)
        ),
    )

    bar = BarCfg(
        height=int(_deep_get(bar_d, "height", BarCfg.height)),
        opacity=float(_deep_get(bar_d, "opacity", BarCfg.opacity)),
    )

    core = CoreCfg(
        follow_mouse_focus=bool(
            _deep_get(core_d, "follow_mouse_focus", CoreCfg.follow_mouse_focus)
        ),
        wmname=str(_deep_get(core_d, "wmname", CoreCfg.wmname)),
        autostart_script=str(
            _deep_get(core_d, "autostart_script", CoreCfg.autostart_script)
        ),
        wallpaper=str(_deep_get(core_d, "wallpaper", CoreCfg.wallpaper)),
        use_autorandr=bool(_deep_get(core_d, "use_autorandr", CoreCfg.use_autorandr)),
    )

    return TearoomCfg(apps=apps, bar=bar, core=core)
