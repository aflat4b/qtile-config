#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile import layout

import colorschemes.catppuccin.catppuccin_macchiato

# This config contains the layouts configuration

# Common settings for each layout I'm going to use
common_layout_settings = dict(
        border_focus = colors[17][0]
        border_normal = colors[13][0]
        border_width = 2
        margin = 4
        )

#List of layouts
layouts = [
        layout.Max(),
        layout.MonadTall(**common_layout_settings),
        layout.MonadWide(**common_layout_settings),
        layout.Matrix(**common_layout_settings),
        layout.Bsp(**common_layout_settings),
        ]
                         
