#!/usr/bin/env python3
"""Check Qtile keybindings for duplicates and conflicts."""
from __future__ import annotations

import sys
from collections import defaultdict

# Import Qtile modules to check
try:
    from config import keys as config_keys
    from modules.keys import keys, mod
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("💡 Make sure you're in the Qtile config directory")
    sys.exit(1)


def extract_key_info(key: object) -> tuple[str, str]:
    """Extract modifier and key from a Qtile Key object."""
    try:
        modifiers = "+".join(key.modifiers) if key.modifiers else "none"
        key_char = str(key.key)
        return modifiers, key_char
    except AttributeError:
        return "unknown", "unknown"


def check_duplicates() -> None:
    """Check for duplicate keybindings."""
    print("🔍 Checking Qtile keybindings for duplicates...")
    print("=" * 50)

    # Collect all keybindings
    all_keys = []

    # Add main keys (which already include group keys)
    all_keys.extend(keys)

    # Add any additional config keys (if any)
    if "config_keys" in locals():
        all_keys.extend(config_keys)

    # Create a map of key combinations
    key_map: defaultdict[tuple[str, str], list[str]] = defaultdict(list)

    for i, key in enumerate(all_keys):
        try:
            modifiers, key_char = extract_key_info(key)
            key_combo = (modifiers, key_char)

            # Get description or create one
            desc = getattr(key, "desc", f"Key {i+1}")
            key_map[key_combo].append(desc)
        except Exception as e:
            print(f"⚠️  Warning: Could not process key {i+1}: {e}")

    # Check for duplicates
    duplicates_found = False

    for (modifiers, key_char), descriptions in key_map.items():
        if len(descriptions) > 1:
            duplicates_found = True
            print(f"❌ DUPLICATE: {modifiers}+{key_char}")
            for desc in descriptions:
                print(f"   - {desc}")
            print()

    if not duplicates_found:
        print("✅ No duplicate keybindings found!")
    else:
        print("⚠️  Duplicate keybindings detected!")
        print("💡 Consider removing or changing conflicting bindings")

    # Show keybinding summary
    print("\n📊 Keybinding Summary:")
    print(f"   Total keybindings: {len(all_keys)}")
    print(f"   Unique combinations: {len(key_map)}")
    print(
        f"   Duplicate combinations: {sum(1 for descs in key_map.values() if len(descs) > 1)}"
    )


def check_modifier_consistency() -> None:
    """Check for consistent modifier usage."""
    print("\n🔧 Modifier Consistency Check:")
    print("=" * 30)

    print(f"   Main modifier: {mod}")

    # Check for common modifier patterns
    modifier_patterns = defaultdict(int)

    for key in keys:
        try:
            if hasattr(key, "modifiers") and key.modifiers:
                pattern = "+".join(sorted(key.modifiers))
                modifier_patterns[pattern] += 1
        except AttributeError:
            pass

    print("   Modifier patterns found:")
    for pattern, count in sorted(modifier_patterns.items()):
        print(f"     {pattern}: {count} bindings")


def main() -> None:
    """Main function."""
    print("🚀 Qtile Keybinding Checker")
    print("=" * 30)

    try:
        check_duplicates()
        check_modifier_consistency()

        print("\n✅ Keybinding check completed!")
        print("💡 Run this script whenever you modify keybindings")

    except Exception as e:
        print(f"❌ Error during keybinding check: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
