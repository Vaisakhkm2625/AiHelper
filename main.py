import platformdirs 

import configparser
import tkinter as tk
import os
from tkinter import StringVar, OptionMenu, Label, Entry, Button

app_auther = "vaisaskh"
app_name = "aihelper"

config_dir = platformdirs.user_config_dir(app_name,app_auther)
config_file = os.path.join(config_dir,"settings.ini")


print(config_file)


# Function to load settings
def load_settings(config_file):
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
        "keybinding_to_take_screenshot": config.get("SETTINGS", "keybinding_to_take_screenshot", fallback="Ctrl+Shift+C")
    }
    
    return settings

# Function to save settings
def save_settings(config_file, settings):
    config = configparser.ConfigParser()
    config["SETTINGS"] = settings
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)



# Function to create the PyTinker GUI for settings
def create_settings_gui(config_file):
    settings = load_settings(config_file)
    
    root = tk.Tk()
    root.title(app_name)
    
    openai_key_var = StringVar(value=settings["openai_key"])
    ocr_option_var = StringVar(value=settings["ocr_option"])
    start_keybinding_var = StringVar(value=settings["keybinding_to_start_typing"])
    stop_keybinding_var = StringVar(value=settings["keybinding_to_stop_typing"])
    screenshot_keybinding_var = StringVar(value=settings["keybinding_to_take_screenshot"])
    
    # OpenAI Key
    Label(root, text="OpenAI Key").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    Entry(root, textvariable=openai_key_var).grid(row=0, column=1, padx=10, pady=5)
    
    # OCR Option
    Label(root, text="OCR Option").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    OptionMenu(root, ocr_option_var, "tesseract", "openai_vision").grid(row=1, column=1, padx=10, pady=5)
    
    # Keybinding to Start Typing
    Label(root, text="Keybinding to Start Typing").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Entry(root, textvariable=start_keybinding_var).grid(row=2, column=1, padx=10, pady=5)
    
    # Keybinding to Stop Typing
    Label(root, text="Keybinding to Stop Typing").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Entry(root, textvariable=stop_keybinding_var).grid(row=3, column=1, padx=10, pady=5)
    
    # Keybinding to Take Screenshot
    Label(root, text="Keybinding to Take Screenshot").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    Entry(root, textvariable=screenshot_keybinding_var).grid(row=4, column=1, padx=10, pady=5)
    
    # Save Button
    def save():
        settings = {
            "openai_key": openai_key_var.get(),
            "ocr_option": ocr_option_var.get(),
            "keybinding_to_start_typing": start_keybinding_var.get(),
            "keybinding_to_stop_typing": stop_keybinding_var.get(),
            "keybinding_to_take_screenshot": screenshot_keybinding_var.get()
        }
        save_settings(config_file, settings)
        root.destroy()
    
    Button(root, text="Save", command=save).grid(row=5, column=0, columnspan=2, pady=10)
    
    root.mainloop()

# Example usage
create_settings_gui(config_file)









