#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile.config import Group, Match, ScratchPad, DropDown
import re

# This file contains the groups configuration

# List of group names

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of layouts labels (will be displayed on the bar)
group_labels = ["", "󰈮", "", "󰎆", "", "󰭹", "", "󱌣", "󰊴"]

# Default layouts for each group
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

# Defining matches for each group

matches_matrix = [[Match(wm_class = re.compile(r"^(Brave\-browser|brave\-broswer|qbittorrent|qBittorrent)$"))],
                  [Match(wm_class = re.compile(r"^(jetbrains\-idea)$"))],
                  [Match(wm_class = re.compile(r"^(Alacritty|Kitty|xterm|st)$"))],
                  [Match(wm_class = re.compile(r"^(deadbeef)$"))],
                  [Match(wm_class = re.compile(r"^(mpv|vlc)$"))],
                  [Match(wm_class = re.compile(r"^(discord)$"))],
                  [Match(wm_class = re.compile(r"^(Zathura|org.pwmt.zathura|Calibre)$"))],
                  [Match(wm_class = re.compile(r"^(btrfs\-assistant\-bin|Btrfs\ Assistant)$"))],
                  [Match(wm_class = re.compile(r"^(steam|steamwebhelper|minecraft\-launcher)$"))]]

# Initialize the group list
groups = []

# Populating the group list

for i in range(len(group_names)):
    groups.append(Group(name = group_names[i],
                        layout = group_layouts[i],
                        label = group_labels[i],
                        matches = matches_matrix[i]))


