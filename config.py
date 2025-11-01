import os
import subprocess
import libqtile.resources
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from layouts import get_layouts
from colors import return_colors
from keys import get_keys
from mouse import get_mouse
from screen import get_screen

mod="mod4"
#color palette
white, gray, black, darkred, red = return_colors()
#wallpaper

keys = get_keys()
# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


group_personalization = [
        {'icon': '', 'name': '1', 'color': red},
        {'icon': '', 'name': '2', 'color': white},
        {'icon': '', 'name': '3', 'color': red},
        {'icon': '', 'name': '4', 'color': white},
]

groups = [
Group(g['name'], label=g['icon']) for g in group_personalization]

for g in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                g.name,
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            Key(
                [mod, "shift"],
                g.name,
                lazy.window.togroup(g.name, switch_group=True),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
        ]
    )

layouts = get_layouts()

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = get_screen()
# Drag floating layouts.
mouse = get_mouse()

wl_input_rules = {
        "type:touchpad": {
            "natural_scroll": True,
            "tap": "enabled",
            "drag_lock": "enabled"
            }
}

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
