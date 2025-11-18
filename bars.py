#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile import bar
from widgets import my_widgets, widget_defaults
from colorschemes.catppuccin.catppuccin_macchiato import colors

# This file contains my bar configuration

my_bar = bar.Bar(widgets = my_widgets, size = 30, background = colors[0], border_color = colors[2], margin = [4, 0, 4, 0], opacity = 0.95)
                         
