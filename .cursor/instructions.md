You are my linux-desktop customization agent.

Use the rules in .cursor/rules/*.mdc. I’m on Qtile with a modular config in ~/.config/qtile/ and modules/ already contains examples of the intended organization. Target system Python ≥3.10 (not guaranteed newer). I’m keyboard‑driven and terminal‑first: kitty, neovim, zsh, with rofi and eww. I want snappy, distro‑agnostic behavior (Ubuntu now, Arch soon), black/ruff formatting, and thorough type hints.

Goals (do all of this):

Audit & normalize the project layout against the structure in the repo intro (config.py → modules/{theme,utils,apps,groups,keys,layouts,widgets,screens,hooks}.py). Keep modules focused (<~200 lines).

Python compat: ensure all code runs on Python 3.10+ (no features newer than 3.10 unless guarded). Keep from __future__ import annotations, use PEP 604 unions (A | B), and avoid 3.11+‑only typing.

Style/tooling: generate a pyproject.toml with black (line‑length 88) and ruff (E,F,W,I,N,UP,ANN,PL). Configure mypy minimally for the config if you add it, but avoid slow imports.

Distro‑agnostic utils: in modules/utils.py provide which(), first_available(), and shell‑out helpers without hardcoding package managers. Prefer lazy.spawn in keybindings; only use subprocess in hooks when necessary.

Apps & bindings: in modules/apps.py centralize commands for kitty, nvim, rofi, eww, browser (via xdg-open). In modules/keys.py (recreate if incomplete) add ergonomic SUPER‑based bindings:

mod+Return kitty; mod+space rofi drun; mod+n kitty‑nvim; mod+b browser.

hjkl focus, with arrow fallbacks; move/resize under KeyChords (mod+g, mod+r).

reload/restart, close window, power menu (rofi/eww), volume/brightness/player via first_available(["wpctl","pactl"]), brightnessctl, playerctl.

Comment each binding inline with a short note.

Layouts/widgets/screens: set sensible defaults in layouts.py; keep widgets.py minimal if I’m using eww (Clock/GroupBox/WindowName/Systray). In screens.py, build bars/panels per monitor; keep them light and reference theme.py for palette/fonts/gaps.

Hooks: in hooks.py, add startup_once to launch eww (idempotent), and any daemons, with no blocking calls. Add quick error‑open binding to view ~/.local/share/qtile/qtile.log in kitty.

Validation/dev UX: add qtile_check.py that imports all modules to fail fast; a Makefile with validate (ruff, black --check, pyflakes) and fmt (black, ruff --fix).

Docs: produce a short README.md (10–20 lines) explaining the layout, keybindings, and how to reload/debug.

Safety: ensure no sudo in hooks or keybinds; no secrets in repo; power/session actions are clearly marked.

Deliverables:

pyproject.toml

modules/{theme,utils,apps,groups,keys,layouts,widgets,screens,hooks}.py (update or generate; keep within 3.10 constraints)

qtile_check.py, Makefile, and a concise README.md

Constraints & style:

Full type hints where practical, but compatible with 3.10.

Black/ruff clean on first pass.

Expressive names, no wildcard imports, minimal comments (self‑documenting first).

Keep startup fast; avoid heavy polling in Python—prefer shell tools.

If anything is missing (e.g., modules/keys.py looks stubbed), recreate it following the rules and explain the key choices at the top of each file in a brief comment.
