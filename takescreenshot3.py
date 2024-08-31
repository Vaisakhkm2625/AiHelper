
from pynput import mouse, keyboard
from PIL import ImageGrab
import threading

# Global variables to store the coordinates
start_x = start_y = end_x = end_y = None
hotkey = '<ctrl>+<alt>+k'  # Define the hotkey (Ctrl+Alt+S)

def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y
    if pressed:
        # Record the start position when mouse is pressed
        start_x, start_y = x, y
    else:
        # Record the end position when mouse is released
        end_x, end_y = x, y
        # Stop listener
        return False

def crop_screenshot(img, start_x, start_y, end_x, end_y):
    # Normalize coordinates (make sure start is top-left, end is bottom-right)
    left = min(start_x, end_x)
    top = min(start_y, end_y)
    right = max(start_x, end_x)
    bottom = max(start_y, end_y)
    
    # Crop the image using the specified coordinates
    cropped_img = img.crop((left, top, right, bottom))
    print("saving cropped screenshot")
    cropped_img.save("cropped_screenshot.png")  # Save the cropped screenshot

def take_and_crop_screenshot():
    # Take a full-screen screenshot
    full_screenshot = ImageGrab.grab()

    # Collect mouse events until released
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # Once mouse listener is done, crop the screenshot
    if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
        crop_screenshot(full_screenshot, start_x, start_y, end_x, end_y)
    else:
        print("No area selected.")

def on_activate():
    print("Hotkey activated! Taking screenshot...")
    screenshot_thread = threading.Thread(target=take_and_crop_screenshot)
    screenshot_thread.start()

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

if __name__ == "__main__":
    # Define a hotkey listener
    with keyboard.GlobalHotKeys({hotkey: on_activate}) as listener:
        listener.join()
