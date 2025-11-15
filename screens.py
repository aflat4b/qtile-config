#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile.config import Screen
from bars import my_bar

# This file contains my screen configuration

my_screen = Screen(top = my_bar),
screens = [my_screen]

                         
