#    _     __ _       _   
#   / \   / _| | __ _| |_ 
#  / _ \ | |_| |/ _` | __|
# / ___ \|  _| | (_| | |_ 
#/_/   \_\_| |_|\__,_|\__|

from libqtile import widget,bar

from colorschemes.catppuccin.catppuccin_macchiato import colors
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
            urgent_alert_method = 'text',
            urgent_text = colors[21],
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
            format = '  {load_percent}%',
            background = colors[0],
            foreground = colors[21],
            update_interval = 1.0
            ),
        widget.Memory(
            **widget_defaults,
            format = '  {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            background = colors[0],
            foreground = colors[19],
            measure_mem = 'M',
            update_interval = 1.0
            ),
        widget.ThermalSensor(
            **widget_defaults,
            format = ' {temp: .1f} {unit}',
            background = colors[0],
            foreground = colors[22],
            foreground_alert = colors[24],
            threshold = 65,
            metric = True,
            ),
        widget.Battery(
            **widget_defaults,
            format = '{char} 󰁹:{percent: 2.0%}',
            battery = 0,
            charging_char = '',
            discharging_char = '󰠠',
            empty_char = '',
            full_char = '',
            background = colors[0],
            foreground = colors[17],
            low_background = colors[0],
            low_foreground = colors[18],
            ),
        widget.Net(
            **widget_defaults,
            format = '  {interface}: {down:6.2f}  {up:6.2f}',
            background = colors[0],
            foreground = colors[12],
            interface = 'wlp0s20f3',
            ),
        widget.Clock(
            **widget_defaults,
            format = '%d/%m%Y %H:%M:%S',
            background = colors[0],
            foreground = colors[14],
            ),
        widget.Backlight(
            **widget_defaults,
            format = '󰃝 {percent:2.0}%',
            backlight_name = 'intel_backlight',
            backlight_file = 'brightness',
            background = colors[0],
            foreground = colors[20],
            ),
        widget.Systray(
            background = colors[0],
            icon_size = 20,
            padding = 5
            ),
        ]
