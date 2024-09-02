import os
import configparser

# Function to load settings
def load_settings(config_file,app_name):
    config = configparser.ConfigParser()

    config_dir=os.path.dirname(config_file)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if not os.path.exists(config_file):
        config["SETTINGS"] = {
            "openai_key": "",
            "ocr_option": "tesseract",
            "keybinding_to_start_typing": "Ctrl+Shift+S",
            "keybinding_to_stop_typing": "Ctrl+Shift+X",
            "keybinding_to_take_screenshot": "Ctrl+Shift+C"
        }
        with open(config_file, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(config_file)

    
    settings = {
        "openai_key": config.get("SETTINGS", "openai_key", fallback=""),
        "ocr_option": config.get("SETTINGS", "ocr_option", fallback="tesseract"),
        "keybinding_to_start_typing": config.get("SETTINGS", "keybinding_to_start_typing", fallback="Ctrl+Shift+S"),
        "keybinding_to_stop_typing": config.get("SETTINGS", "keybinding_to_stop_typing", fallback="Ctrl+Shift+X"),
        "keybinding_to_take_screenshot": config.get("SETTINGS", "keybinding_to_take_screenshot", fallback="Ctrl+Shift+C"),
        "fake_app_name": config.get("SETTINGS", "fake_app_name", fallback=app_name)
    }
    
    return settings



# Function to save settings
def save_settings(config_file, settings):
    config = configparser.ConfigParser()
    config["SETTINGS"] = settings
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)
