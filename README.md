# Qtile Configuration

Modular Qtile configuration with keyboard-driven workflow, designed for ultrawide monitors and multiple screens.

## Layout

```
~/.config/qtile/
├── config.py              # Main configuration (imports modules)
├── modules/               # Modular components
│   ├── theme.py          # Colors, fonts, spacing
│   ├── utils.py          # Distro-agnostic utilities
│   ├── apps.py           # Application commands
│   ├── keys.py           # Keybindings and shortcuts
│   ├── layouts.py        # Window layouts
│   ├── widgets.py        # Bar widgets (minimal)
│   ├── screens.py        # Multi-monitor bars
│   ├── groups.py         # Workspace groups
│   └── hooks.py          # Startup and event hooks
├── scripts/               # Helper shell scripts
├── qtile_check.py         # Configuration validation
└── Makefile              # Development tasks
```

## Keybindings

### Organization
The keybindings are organized into logical groups for easy management:
- **app_launchers**: Terminal, browser, file manager, launchers
- **system_actions**: Close, reload, shutdown, lock, screenshot
- **navigation_keys**: Vim-style window focus navigation
- **window_management**: Move windows, layout control, floating
- **window_resize**: Resize operations (Super+Ctrl+h/j/k/l)
- **media_controls**: Volume, media transport, brightness with notifications

To disable a group, comment out its line in the merge section of `modules/keys.py`.

### Core Navigation
- `Super+Return` - Launch kitty terminal
- `Super+Space` - Rofi application launcher (drun)
- `Super+b` - Launch Firefox directly
- `Super+f` - Open file manager
- `Super+BackSpace` - Rofi window switcher

### Window Management
- `Super+h/j/k/l` - Navigate windows (vim-style)
- `Super+Shift+h/j/k/l` - Move windows
- `Super+Ctrl+h/j/k/l` - Resize windows (your working setup!)
- `Super+Ctrl+Shift+h/l` - Shrink columns
- `Super+Tab` - Next layout
- `Super+q` - Close window
- `Super+Shift+f` - Toggle floating

### Mouse Behavior
- **Click to Focus**: Windows only activate when clicked (no mouse-following)
- **Active Window Border**: Bright purple border (`#a855f7`) around focused windows - 4px wide
- **Resize/Move**: Hold `Super` + drag for window operations

### System Controls
- `Super+Ctrl+r` - Reload Qtile configuration
- `Super+Ctrl+q` - Shutdown Qtile
- `Super+Shift+z` - Lock screen
- `Super+Shift+s` - Take screenshot
- `Super+Ctrl+o` - View Qtile log in kitty

### Power Management (No Confirmation - Hard to Press Accidentally)
- `Super+Alt+Ctrl+Escape` - Suspend system
- `Super+Alt+Ctrl+Return` - Shutdown system
- `Super+Alt+Ctrl+r` - Reboot system
- `Super+Alt+Ctrl+l` - Logout Qtile
- `Super+Alt+Ctrl+p` - Power menu (rofi)

### Media Controls (with visual feedback)
- Volume keys - Volume control with notifications
- Media transport - Player controls with notifications
- Brightness keys - Brightness control with notifications

## Development

### Quick Start
```bash
# Install development tools
make install

# Format and validate
make dev

# Quick validation
make quick-validate
```

### Available Commands
- `make fmt` - Format code with black and ruff
- `make check` - Run linting and formatting checks
- `make validate` - Full configuration validation (includes duplicate keybinding check)
- `make check-keys` - Check keybindings for duplicates only
- `make clean` - Remove Python cache files

## Reload & Debug

### Reload Configuration
```bash
# From terminal
qtile cmd-obj -o cmd -f reload_config

# Or use keybinding: Super+Ctrl+r
```

### View Logs
```bash
# View Qtile log
kitty -e nvim ~/.local/share/qtile/qtile.log

# Or use keybinding: Super+Ctrl+o
```

### Troubleshooting
1. Run `python3 qtile_check.py` to validate imports
2. Check `~/.local/share/qtile/qtile.log` for errors
3. Use `make validate` for comprehensive checks

## Features

- **Modular Design**: Clean separation of concerns
- **Keyboard-First**: Vim-style navigation with arrow fallbacks
- **Multi-Monitor**: Adaptive bars per screen
- **Distro-Agnostic**: Works on Ubuntu, Arch, and others
- **Type Safe**: Full Python 3.10+ type hints
- **Fast Startup**: Minimal Python overhead
- **Group 1 Default**: Uses MonadThreeCol layout for ultrawide
- **Working Resize**: Restored your Super+Ctrl+h/j/k/l resize setup
- **Visual Feedback**: Notifications for media controls
- **Direct Firefox**: Launches Firefox directly, not new tabs
- **Duplicate-Free**: Automatic keybinding conflict detection
- **Organized Keys**: Named keybinding groups for easy management
