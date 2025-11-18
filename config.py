#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

import os

from libqtile import layout
from keys import keys, mouse
from groups import groups
from layouts import layouts
from screens import screens
from bars import my_bar
from widgets import widget_defaults, my_widgets
from rules import dgroups_app_rules

# This is the main entry of my qtile config



dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
focus_on_window_activation = 'smart'
wmname = 'qtile'
                         
