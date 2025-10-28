from libqtile.config import Screen
from libqtile import bar
from colors import return_colors
from custom_widgets import get_widgets

def get_screen():
    white, gray, black, darkred, red = return_colors()
    wallpaper = '~/Imágenes/wallpaperflare.com_wallpaper.jpg'
    return [
    Screen(
        top=bar.Bar(
           get_widgets(), 
            24,
            border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        border_color=[red, red, red, red],  # Borders are magenta
        background=black,
        margin=[1, 0, 0, 0],
        ),
        wallpaper=wallpaper,
        wallpaper_mode="center",
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
        ),
    ]


