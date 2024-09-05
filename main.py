from pystray import Menu,MenuItem,Icon

import os
from PIL import Image, ImageDraw
from generate_penguin_logo import draw_penguin_logo
from settings import load_settings, save_settings
import platformdirs



app_auther = "vaisaskh"
app_name = "aihelper"
fake_app_name = app_name

config_dir = platformdirs.user_config_dir(app_name,app_auther)
config_file = os.path.join(config_dir,"settings.ini")

print(config_file)


settings = load_settings(config_file,app_name)

def stop_hotkeys():
    print("helllosa")
def start_hotkeys():
    pass

icon = Icon(
    'Start Listening',
    icon=draw_penguin_logo(64, 64),
    menu=Menu(
        MenuItem('Start Hotkeys', start_hotkeys),
        MenuItem('Stop Hotkeys', stop_hotkeys),
        MenuItem('Quit', lambda: icon.stop())
    )
)

icon.run()

