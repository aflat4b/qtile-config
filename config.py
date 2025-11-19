#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

import os, subprocess
from libqtile import layout, hook
from keys import keys, mouse
from groups import groups
from layouts import layouts
from screens import screens
from bars import my_bar
from widgets import widget_defaults, my_widgets
from rules import dgroups_app_rules
from colorschemes.catppuccin.catppuccin_macchiato import colors

# This is the main entry of my qtile config

# Startup hook

@hook.subscribe.startup_once
def autostart():
    script = os.path.expandusers("~/.config/autostart/autostart.sh")
    subprocess.run(script)

# Qtile variables
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus = colors[17][0],
                                  border_normal = colors[13][0],
                                  border_width = 2,
                                  fullscreen_border_width = 2)
focus_on_window_activation = 'smart'
wmname = 'LG3D'
                         
