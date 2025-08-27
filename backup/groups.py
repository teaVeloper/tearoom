"""
groups.py
"""

from libqtile import hook, qtile
from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.lazy import lazy

from keys import keys, mod

groups = [
    Group(
        "1",
        label="",
        layout="monadthreecol",
    ),
    Group(
        "2",
        label="",
        layout="max",
    ),
    Group(
        "3",
        label="",
        layout="max",
    ),
    Group("4", label="", layout="columns"),
    Group("5", label="💬", layout="monadthreecol"),
    Group("6", layout="columns"),
    Group("7", layout="columns"),
    Group("8", layout="columns"),
    Group("9", layout="columns"),
]

# groups = [Group(str(i)) for i in range(1, 10)]
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc=f"Send to group {i.name}",
            ),
        ]
    )
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty",
                width=0.6,
                height=0.5,
                x=0.2,
                y=0.1,
                opacity=0.95,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "ranger",
                "kitty -e ranger",
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.1,
                opacity=0.95,
            ),
        ],
    )
)


@hook.subscribe.client_managed
def limit_group1_clients(client):
    if client.group.name == "1":
        if len(client.group.windows) > 5:
            for g in groups:
                if (
                    g.name not in ["1", "scratchpad"]
                    and len(qtile.groups_map[g.name].windows) == 0
                ):
                    client.togroup(g.name)
                    break
