#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile.config import Group, Match, ScratchPad, Dropdown

# This file contains the groups configuration

# List of layouts names (will be displayed on the bar)
group_names = ["", "󰈮", "", "󰎆", "", "󰭹", "", "󱌣", "󰊴"]

# Default layouts for each group
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

# Defining matches for each group

matches_matrix = [[Match(wm_class = ["Brave-broswer", "brave-browser", "qbittorrent", "qBittorrent"])],
                  [Match(wm_class = ["jetbrains-idea"])]
                  [Match(wm_class = ["Alacritty", "Kitty", "xterm", "st"])],
                  [Match(wm_class = ["deadbeef"])],
                  [Match(wm_class = ["mpv", "vlc"])],
                  [Match(wm_class = ["discord"])],
                  [Match(wm_class = ["Zathura", "org.pwmt.zathura", "Calibre"])],
                  [Match(wm_class = ["btrfs-assistant-bin", "Btrfs Assistant"])],
                  [Match(wm_class = ["steam", "steamwebhelper", "minecraft-launcher"])]]

# Initialize the group list
groups = []

# Populating the group list

for i in range(len(group_names)):
    groups.append(Group(name = group_names[i],
                        layout = group_layouts[i],
                        matches = matches_matrix[i]))


