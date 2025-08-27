#!/usr/bin/env python3
"""Python-based layout switcher for Qtile using rofi."""
from __future__ import annotations
import subprocess
import sys
from typing import List


def get_qtile_layouts() -> List[str]:
    """Get available layouts from Qtile."""
    try:
        result = subprocess.run(
            ["qtile", "cmd-obj", "-o", "layout", "-f", "layouts"],
            capture_output=True,
            text=True,
            check=True
        )
        
        layouts = []
        for line in result.stdout.strip().split('\n'):
            if ':' in line:
                layout_name = line.split(':', 1)[1].strip()
                layouts.append(layout_name)
        
        return layouts
    except subprocess.CalledProcessError:
        print("❌ Error getting layouts from Qtile")
        return []


def show_rofi_menu(layouts: List[str]) -> str | None:
    """Show rofi menu and return selected layout."""
    if not layouts:
        return None
    
    # Create rofi input
    rofi_input = '\n'.join(layouts)
    
    try:
        result = subprocess.run(
            ["rofi", "-dmenu", "-p", "Switch to layout:", "-i"],
            input=rofi_input,
            text=True,
            capture_output=True,
            check=True
        )
        
        selected = result.stdout.strip()
        return selected if selected else None
    except subprocess.CalledProcessError:
        return None


def switch_to_layout(layout_name: str, layouts: List[str]) -> None:
    """Switch to the selected layout."""
    try:
        layout_index = layouts.index(layout_name)
        subprocess.run(
            ["qtile", "cmd-obj", "-o", "layout", "-f", "switch_to", str(layout_index)],
            check=True
        )
        print(f"✅ Switched to {layout_name}")
    except ValueError:
        print(f"❌ Layout {layout_name} not found")
    except subprocess.CalledProcessError:
        print(f"❌ Error switching to {layout_name}")


def main() -> None:
    """Main function."""
    layouts = get_qtile_layouts()
    
    if not layouts:
        print("❌ No layouts available")
        sys.exit(1)
    
    selected = show_rofi_menu(layouts)
    
    if selected:
        switch_to_layout(selected, layouts)
    else:
        print("ℹ️  No layout selected")


if __name__ == "__main__":
    main()
