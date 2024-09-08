
from pystray import Menu, MenuItem, Icon
from pynput import keyboard
import os
from PIL import Image, ImageDraw
from generate_penguin_logo import draw_penguin_logo
from settings import load_settings, save_settings
import ui
import platformdirs


app_auther = "vaisaskh"
app_name = "aihelper"
fake_app_name = app_name

config_dir = platformdirs.user_config_dir(app_name, app_auther)
config_file = os.path.join(config_dir, "settings.ini")

print(config_file)

settings = load_settings(config_file, app_name)


# Key press/release event handlers
def on_activate_h():
    print('<ctrl>+<alt>+h pressed')
    listener = keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True)
    listener.start()

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')
    print('Listener stopped')

def on_press(key):
    print(f"Key pressed: {key}")

def on_release(key):
    print(f"Key released: {key}")


# Function to start hotkeys, passing the keyboard_instance as an argument
def start_hotkeys(keyboard_instance):
    if keyboard_instance is None:
        keyboard_instance = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+h': on_activate_h,
            '<ctrl>+<alt>+i': on_activate_i
        })
        keyboard_instance.start()
        print("Hotkeys enabled")
    return keyboard_instance


# Function to stop hotkeys, passing the keyboard_instance as an argument
def stop_hotkeys(keyboard_instance):
    if keyboard_instance:
        keyboard_instance.stop()
        print("Hotkeys disabled")
    return None


# Function to toggle hotkeys, maintaining state internally
def toggle_hotkeys(hotkeys_active, keyboard_instance):
    if hotkeys_active:
        keyboard_instance = stop_hotkeys(keyboard_instance)
        hotkeys_active = False
    else:
        keyboard_instance = start_hotkeys(keyboard_instance)
        hotkeys_active = True
    return hotkeys_active, keyboard_instance


# Create a checkbox item for the tray icon menu
def create_checkbox_item(label, action, state_getter):
    return MenuItem(
        label,
        action,
        checked=lambda _: state_getter(),  # Checkbox state
        #toggle=True  # Enables checkbox functionality
    )


# State management variables for hotkeys (these will be passed into functions)
hotkeys_active = False
keyboard_instance = None

# Toggle hotkeys function that updates the state
def toggle_hotkeys_menu():
    global hotkeys_active, keyboard_instance
    hotkeys_active, keyboard_instance = toggle_hotkeys(hotkeys_active, keyboard_instance)


# System tray icon
icon = Icon(
    'Start Listening',
    icon=draw_penguin_logo(64, 64),
    menu=Menu(
        create_checkbox_item('Enable Hotkeys', toggle_hotkeys_menu, lambda: hotkeys_active),
        MenuItem('Show Settings', ui.create_settings_gui),
        MenuItem('Quit', lambda: icon.stop())
    )
)

icon.run()
