#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

import re
from libqtile.config import Match, Rule

# This file contains my floating rules
dgroups_app_rules = [
        Rule(Match(wm_type = re.compile(r"^(confirm|"\
                "download|"\
                "notification|"\
                "toolbar|"\
                "splash|"\
                "dialog|"\
                "error|"\
                "file_progress|"\
                "confirmreset|"\
                "makebranch|"\
                "maketag|"\
                "branchdialog|"\
                "pinentry|"\
                "sshaskpass|)$")), float = True),

        Rule(Match(wm_class = re.compile(r"^(blueman\-manager|"\
                "Blueman\-manager|"\
                "nm\-connection\-editor|"\
                "Nm\-connection\-editor|"\
                "lxappearance|"\
                "Lxappearance|"\
                "pavucontrol|"\
                "Virtualbox|"\
                "arandr|"\
                "Arandr|"\
                "qt6ct)$")), float = True)
             ]
