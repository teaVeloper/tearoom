from __future__ import annotations

from pathlib import Path

from tearoom.display.trandr import trandr_env, trandr_profiles_dir, trandr_repo_root


def test_trandr_paths_default_from_teagarden(monkeypatch) -> None:
    monkeypatch.delenv("TRANDR_PROFILES_DIR", raising=False)
    monkeypatch.setenv("TEAGARDEN_HOME", "/tmp/teagarden")

    assert trandr_repo_root() == Path("/tmp/teagarden/trandr")
    assert trandr_profiles_dir() == Path("/tmp/teagarden/trandr/profiles")


def test_trandr_env_preserves_explicit_overrides(monkeypatch) -> None:
    monkeypatch.setenv("TRANDR_PROFILES_DIR", "/tmp/custom-trandr/profiles")

    env = trandr_env()

    assert env["TRANDR_PROFILES_DIR"] == "/tmp/custom-trandr/profiles"
