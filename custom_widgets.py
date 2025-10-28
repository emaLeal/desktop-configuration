from libqtile import qtile, widget
from colors import return_colors

white, gray, black, darkred, red = return_colors()

def get_widgets():
    return [
        widget.GroupBox(
            active=red,
            block_highlight_text_color=white,
            borderwidth=2,
            fontsize=18,
            inactive=white,
            this_current_screen_border=darkred,
            highlight_method='line',
            background_color=black,
            margin_y=3,
            margin_x=0,
            padding_y=6,
            padding_x=8,
            highlight_color=[red, gray]
        ),
        widget.Prompt(),
        widget.WindowName(),
        widget.Notify(),
        widget.NetGraph(),
        widget.Chord(
            chords_colors={
                "launch": (red, white),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.Battery(
            format='{char}    {percent:2.0%}',
            full_char='',
            charge_char='',
            discharge_char='',
            empty_char='',
            low_foreground=red,
            low_percentage=0.2
        ),
        widget.PulseVolume(
            emoji=True,
            emoji_list=['','']
            ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
        widget.Systray(),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(
            default_text='',
            countdown_start=3
            ),
    ]
