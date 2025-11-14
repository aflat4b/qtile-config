#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile import widget

import colorschemes.catppuccin.catppuccin_macchiato

# This file contains the list of widgets I use

widget_defaults = dict(
        font = "Mononoki Nerd Font",
        fontsize = 16,
        padding = 5
        )

my_widgets = [
        widget.GroupBox(
            **widget_defaults,
            hide_unused = True,
            disable_drag = True,
            highlight_method = 'text',
            background = colors[0],
            foreground = colors[11],
            active = colors[15],
            inactive = colors[8],
            this_current_screen_border = colors[18],
            ),
        widget.WindowName(
            **widget_defaults,
            max_chars = 80,
            empty_group_string = 'Aflat\'s desktop',
            background = colors[0],
            foreground = colors[11],
            ),
        widget.CurrentLayout(
            **widget_defaults,
            background = colors[0],
            foreground = colors[11],
            ),
        widget.Spacer(
            length = bar.STRETCH
            ),
        widget.CPU(
            **widget_defaults,
            ),
        widget.Memory(
            **widget_defaults,
            ),
        widget.Battery(
            **widget_defaults
            ),
        widget.Net(
            **widget_defaults
            ),
        widget.Backlight(
            **widget_defaults
            ),
        widget.Systray()
        ]
