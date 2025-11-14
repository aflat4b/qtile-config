#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile.config import Match, Rule

# This file contains my floating rules
dgroups_app_rules = [
        Rule(Match(wm_type = [
            "confirm",
			"download",
			"notification",
			"toolbar",
			"splash",
			"dialog",
			"error",
			"file_progress",
			"confirmreset",
			"makebranch",
			"maketag",
			"branchdialog",
			"pinentry",
			"sshaskpass"
            ]), float = True),

        Rule(Match(wm_class = [
            "blueman-manager",
            "Blueman-manager",
            "nm-connection-editor",
            "Nm-connection-editor",
            "lxappearance",
            "Lxappearance",
            "pavucontrol",
            "Virtualbox",
            "arandr",
            "Arandr",
            "qt6ct"
            ], float = True)
             ]
