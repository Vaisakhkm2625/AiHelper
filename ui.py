import platformdirs 
import os
import tkinter as tk
from tkinter import StringVar, OptionMenu, Label, Entry, Button
from settings import load_settings, save_settings


app_auther = "vaisaskh"
app_name = "aihelper"
fake_app_name = app_name

config_dir = platformdirs.user_config_dir(app_name,app_auther)
config_file = os.path.join(config_dir,"settings.ini")

print(config_file)



# Function to create the PyTinker GUI for settings
def create_settings_gui(config_file):
    settings = load_settings(config_file,app_name)
    
    root = tk.Tk()
    root.title(fake_app_name)
    
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
if __name__ == "__main__":
    create_settings_gui(config_file)









