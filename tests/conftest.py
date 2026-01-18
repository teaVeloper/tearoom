from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QTILE_DIR = ROOT / "qtile"

# Make `import tearoom...` resolve to ./qtile/tearoom
sys.path.insert(0, str(QTILE_DIR))
