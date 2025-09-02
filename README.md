# Qtile Configuration

Modular Qtile configuration with Python 3.10+ compatibility, Black/Ruff formatting, and comprehensive type hints.

## Project Structure

```
~/.config/qtile/
├── config.py              # Main configuration (imports from modules/)
├── modules/               # Modular configuration components
│   ├── theme.py          # Color palette, fonts, spacing
│   ├── utils.py          # Distro-agnostic helper functions
│   ├── apps.py           # Application commands and launchers
│   ├── groups.py         # Workspace groups and scratchpads
│   ├── keys.py           # Keybindings and mouse bindings
│   ├── layouts.py        # Window layouts and floating rules
│   ├── widgets.py        # Qtile bar widgets
│   ├── screens.py        # Multi-monitor bar configuration
│   └── hooks.py          # Startup, shutdown, and event hooks
├── bin/                   # Qtile runtime helper scripts
│   ├── volume.sh         # Volume control
│   ├── power-menu.sh     # Power management
│   ├── layout_switcher.py # Layout switching via Rofi
│   ├── fix-keyboard-system.sh # Runtime keyboard fix
│   └── check-devices.sh  # Input device diagnostics
├── setup/                 # Installation and setup scripts
│   ├── install-keyboard-fix-systemd.sh # Systemd service install
│   └── install-keyboard-fix-udev.sh    # Udev rules install
└── scripts/               # Legacy scripts (deprecated)
```

## Keybindings

### Application Launchers
- `Super+Return` - Launch kitty terminal
- `Super+Space` - Rofi application launcher
- `Super+b` - Launch Firefox browser
- `Super+f` - Open file manager in current directory

### Window Management
- `Super+h/j/k/l` - Focus windows (vim-style)
- `Super+Shift+h/j/k/l` - Move windows between layouts
- `Super+Ctrl+h/j/k/l` - Resize windows
- `Super+Shift+f` - Toggle floating
- `Super+n` - Reset layout

### Layout & Groups
- `Super+Tab` - Next layout
- `Super+Shift+Tab` - Previous layout
- `Super+Shift+g` - Rofi layout switcher
- `Super+1-9` - Switch to workspace groups

### Power Management
- `Super+Alt+Ctrl+Escape` - Suspend
- `Super+Alt+Ctrl+Return` - Shutdown
- `Super+Alt+Ctrl+r` - Reboot
- `Super+Alt+Ctrl+l` - Logout

### Media Controls
- `XF86Audio*` - Volume control (with visual feedback)
- `XF86MonBrightness*` - Brightness control
- `Print` - Screenshot

## Mouse Behavior

- **Click-to-focus only** - Mouse movement doesn't steal focus
- **Visible active window** - Bright purple border (4px) for active windows
- **Window resizing** - Mod+LeftButton drag to resize, Mod+MiddleButton drag to move

## Development

```bash
# Format and lint
make fmt

# Check code quality
make check

# Validate configuration
make validate

# Quick validation
make quick-validate

# Check keybindings
make check-keys
```

## Reload & Debug

- **Reload**: `Super+Ctrl+r` (reloads configuration)
- **Restart**: `Super+Ctrl+q` (restarts Qtile)
- **View logs**: `Super+Ctrl+o` (opens Qtile log in kitty)

## Features

- **Modular configuration** - Easy to maintain and extend
- **Multi-monitor support** - Automatic bar configuration per screen
- **Tokyo Night theme** - Dark theme with purple accents
- **Distro-agnostic** - Works on Ubuntu, Arch, and other distributions
- **Fast startup** - No blocking operations during import
- **Type safety** - Full Python 3.10+ type hints throughout
