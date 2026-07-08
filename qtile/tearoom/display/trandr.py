from __future__ import annotations

import importlib
import logging
import os
from pathlib import Path
import shutil
import subprocess
import sys
from types import ModuleType

LOG = logging.getLogger(__name__)

_LAPTOP_POSITIONS = {"left", "right", "up", "down"}
_PRIMARY_CHOICES = {"laptop", "external"}


def _teagarden_home() -> Path:
    root = os.environ.get("TEAGARDEN_HOME")
    if root:
        return Path(root).expanduser().resolve()
    return Path.home() / "src" / "teagarden"


def trandr_repo_root() -> Path:
    override = os.environ.get("TRANDR_REPO_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return (_teagarden_home() / "trandr").resolve()


def trandr_profiles_dir() -> Path:
    override = os.environ.get("TRANDR_PROFILES_DIR")
    if override:
        return Path(override).expanduser().resolve()
    return (trandr_repo_root() / "profiles").resolve()


def trandr_env() -> dict[str, str]:
    env = os.environ.copy()
    profiles_dir = trandr_profiles_dir()
    if profiles_dir.exists():
        env.setdefault("TRANDR_PROFILES_DIR", str(profiles_dir))
    return env


def _sibling_src_dir() -> Path:
    return trandr_repo_root() / "src"


def _load_qtile_module() -> ModuleType | None:
    env = trandr_env()
    if "TRANDR_PROFILES_DIR" in env:
        os.environ.setdefault("TRANDR_PROFILES_DIR", env["TRANDR_PROFILES_DIR"])

    try:
        return importlib.import_module("trandr.qtile")
    except ModuleNotFoundError:
        pass

    sibling_src = _sibling_src_dir()
    if sibling_src.exists():
        sys.path.insert(0, str(sibling_src))
        try:
            return importlib.import_module("trandr.qtile")
        except ModuleNotFoundError:
            return None
    return None


def cli_available() -> bool:
    return shutil.which("trandr") is not None


def available() -> bool:
    return _load_qtile_module() is not None or cli_available()


def _warn_unavailable() -> None:
    LOG.warning(
        "trandr is not available. Install the system package or keep the repo at %s.",
        trandr_repo_root(),
    )


def apply_profile(name: str, *, check: bool = False) -> bool:
    module = _load_qtile_module()
    if module is not None:
        module.apply_profile(name, check=check)
        return True
    if cli_available():
        subprocess.run(
            ["trandr", "apply", "--profile", name],
            check=check,
            env=trandr_env(),
        )
        return True
    _warn_unavailable()
    return False


def infer_and_apply(
    laptop_position: str,
    *,
    primary: str = "laptop",
    check: bool = False,
) -> bool:
    if laptop_position not in _LAPTOP_POSITIONS:
        raise ValueError(f"unsupported laptop position: {laptop_position}")
    if primary not in _PRIMARY_CHOICES:
        raise ValueError(f"unsupported primary target: {primary}")

    module = _load_qtile_module()
    if module is not None:
        module.apply_inferred(laptop=laptop_position, primary=primary, check=check)
        return True
    if cli_available():
        subprocess.run(
            [
                "trandr",
                "infer",
                "--laptop",
                laptop_position,
                "--primary",
                primary,
                "--apply",
            ],
            check=check,
            env=trandr_env(),
        )
        return True
    _warn_unavailable()
    return False
