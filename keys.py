#    _      __  _         _   
#   / \    / _|| |  __ _ | |_ 
#  / _ \  | |_ | | / _` || __|
# / ___ \ |  _|| || (_| || |_ 
#/_/   \_\|_|  |_| \__,_| \__|


from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy

from groups import groups

# This file contains the keybindings for my qtile configuration

# Defining mod key as the super key
mod = "mod4"

# Aliasing the mod1 key to the alt key
alt = "mod1"

# Alias for dmenu command
dmenu = "dmenu_run -fn 'Mononoki Nerd Font:pixelsize=16' -nb #24273a -nf #a6da95 -sb #a6da95 -sf #24273a -p 'EXEC:'"

# Alias for terminal
terminal = "alacritty"

keys = [
        # Terminal and Dmenu keybindings
        Key([mod], "t", lazy.spawn(terminal), desc="Spawn terminal"),
        Key([mod], "d", lazy.spawn(dmenu), desc="Spawn dmenu"),

        # Closing window
        Key([mod, "shift"], "q", lazy.window.kill()),

        # Monitor brightness control
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),

        # Keyboard brightness control
        Key([], "XF86KbdBrightnessUp", lazy.spawn("brightnessctl -d 'rgb*' s 5%+")),
        Key([], "XF86KbdBrightnessDown", lazy.spawn("brightnessctl -d 'rgb*' s 5%-")),
        Key([], "XF86KbdLightOnOff", lazy.spawn("brightnessctl -d 'rgb*' s 0%")),

        # Volume control
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset 'Master' 5%+")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset 'Master' 5%-")),
        Key([], "XF86AudioMute", lazy.spawn("amixer sset 'Master' toggle")),

        # Making the focusing window float
        Key([mod], "space", lazy.window.toggle_floating()),
        Key([mod], "f", lazy.window.toggle_fullscreen()),

        # Reloading qtile config
        Key([mod, "shift"], "r", lazy.restart()),
        Key([mod, "control"], "r", lazy.reload_config()),
        Key([mod, "control"], "q", lazy.shutdown()),

        # Layout keybindings
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod, "shift"], "n", lazy.layout.normalize(), desc = "Normalize layout"),
        Key([mod, "control"], "space", lazy.next_layout()),
 
        # MonadTall and MonadWide specific
        Key([mod, "shift"], "h", lazy.layout.swap_left(), desc = "Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.swap_right(), desc = "Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc = "Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc = "Move window up"),

        Key([mod], "i", lazy.layout.grow(), desc = "Grows master area"),
        Key([mod], "m", lazy.layout.shrink(), desc = "Shrinks master area"),
        Key([mod], "n", lazy.layout.reset(), desc = "Resets master area to defaults"),
        Key([mod], "o", lazy.layout.normalize(), desc = "Normalizes layout"),
        Key([mod, "shift"], "space", lazy.layout.flip(), desc = "Flips layout"),

        # Bsp specific
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc = "Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc = "Move window to the right"),
        Key([mod, alt], "j", lazy.layout.flip_down(), desc = "Flips layout down"),
        Key([mod, alt], "k", lazy.layout.flip_up(), desc = "Flips layout up"),
        Key([mod, alt], "h", lazy.layout.flip_left(), desc = "Flips layout left"),
        Key([mod, alt], "l", lazy.layout.flip_right(), desc = "Flips layout right"),
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc = "Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc = "Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc = "Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc = "Grow window up"),
        ]

# Adding group switching keybindings

for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group = True)))

mouse = [
        # Mouse bindings
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
        ]


                             
