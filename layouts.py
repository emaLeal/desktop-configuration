from colors import return_colors
from libqtile import layout

white, gray, black, darkred, red = return_colors()

def get_layouts():
    return [
        layout.MonadTall(
        border_focus=darkred,
        border_width = 1,
        margin=4
         ),
   ]

