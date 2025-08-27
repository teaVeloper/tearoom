#!/bin/bash
# Rofi Layout Switcher for Qtile
# Shows available layouts and switches to the selected one

set -euo pipefail

# Get available layouts from Qtile
layouts=$(qtile cmd-obj -o layout -f layouts)

# Parse layouts and create rofi menu
layout_list=""
while IFS= read -r line; do
    if [[ $line =~ ^[0-9]+:\ (.+)$ ]]; then
        layout_name="${BASH_REMATCH[1]}"
        layout_list+="${layout_name}\n"
    fi
done <<< "$layouts"

# Show rofi menu and get selection
selected=$(echo -e "$layout_list" | rofi -dmenu -p "Switch to layout:" -i)

if [[ -n "$selected" ]]; then
    # Find the layout index
    layout_index=0
    while IFS= read -r line; do
        if [[ $line =~ ^[0-9]+:\ (.+)$ ]]; then
            layout_name="${BASH_REMATCH[1]}"
            if [[ "$layout_name" == "$selected" ]]; then
                # Switch to the selected layout
                qtile cmd-obj -o layout -f switch_to "$layout_index"
                break
            fi
            ((layout_index++))
        fi
    done <<< "$layouts"
fi
