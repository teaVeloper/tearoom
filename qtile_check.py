#!/usr/bin/env python3
"""Qtile configuration validation script - import all modules to fail fast."""
from __future__ import annotations

import sys
from typing import NoReturn


def validate_imports() -> None:
    """Validate that all Qtile modules can be imported without errors."""
    print("🔍 Validating Qtile configuration modules...")

    # List of modules to validate
    modules = [
        "modules.theme",
        "modules.utils",
        "modules.apps",
        "modules.keys",
        "modules.layouts",
        "modules.widgets",
        "modules.screens",
        "modules.groups",
        "modules.hooks",
        "config",
    ]

    failed_imports = []

    for module_name in modules:
        try:
            __import__(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
            failed_imports.append((module_name, e))
        except Exception as e:
            print(f"⚠️  {module_name}: {e}")
            failed_imports.append((module_name, e))

    if failed_imports:
        print(f"\n❌ Validation failed: {len(failed_imports)} module(s) have errors")
        for module_name, error in failed_imports:
            print(f"   {module_name}: {error}")
        sys.exit(1)

    print(f"\n✅ All {len(modules)} modules imported successfully!")
    print("🎉 Qtile configuration is ready to use")


def check_python_version() -> None:
    """Check Python version compatibility."""
    version = sys.version_info
    print(f"🐍 Python {version.major}.{version.minor}.{version.micro}")

    if version < (3, 10):
        print("❌ Python 3.10+ required")
        sys.exit(1)

    print("✅ Python version compatible")


def main() -> NoReturn:
    """Main validation function."""
    print("🚀 Qtile Configuration Validator")
    print("=" * 40)

    check_python_version()
    print()
    validate_imports()

    print("\n🎯 Configuration validation complete!")
    print("💡 Run 'qtile check' to validate the configuration")
    print("💡 Run 'qtile start' to start Qtile")

    sys.exit(0)


if __name__ == "__main__":
    main()
