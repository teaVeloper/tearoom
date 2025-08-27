"""Utility functions for Qtile configuration - distro-agnostic helpers."""
from __future__ import annotations

import subprocess
from collections.abc import Iterable, Sequence
from pathlib import Path
from shutil import which as _which


def which(cmd: str) -> str | None:
    """Find executable in PATH, returns full path or None."""
    return _which(cmd)


def first_available(candidates: Iterable[str]) -> str | None:
    """Return first available command from candidates list."""
    for cmd in candidates:
        if _which(cmd):
            return cmd
    return None


def shell_out(
    cmd: Sequence[str],
    capture_output: bool = True,
    text: bool = True,
    timeout: int | None = None,
) -> subprocess.CompletedProcess[str]:
    """Execute shell command with error handling."""
    try:
        return subprocess.run(
            cmd, capture_output=capture_output, text=text, timeout=timeout, check=False
        )
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(cmd, -1, "", "Command timed out")


def get_audio_control() -> str | None:
    """Get available audio control command (wpctl or pactl)."""
    return first_available(["wpctl", "pactl"])


def get_brightness_control() -> str | None:
    """Get available brightness control command."""
    return first_available(["brightnessctl", "xbacklight", "light"])


def get_power_control() -> str | None:
    """Get available power control command."""
    return first_available(["systemctl", "loginctl"])


def get_qtile_log_path() -> Path:
    """Get Qtile log file path."""
    return Path.home() / ".local" / "share" / "qtile" / "qtile.log"


def ensure_dir(path: Path) -> None:
    """Ensure directory exists, create if needed."""
    path.mkdir(parents=True, exist_ok=True)
