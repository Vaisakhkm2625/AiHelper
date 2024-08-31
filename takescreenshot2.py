
from pynput import mouse
from PIL import ImageGrab

# Global variables to store the coordinates
start_x = start_y = end_x = end_y = None

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

def on_move(x, y):
    if start_x is not None and start_y is not None:
        # This part could be used to show a live preview or tracking
        pass

def crop_screenshot(img, start_x, start_y, end_x, end_y):
    # Normalize coordinates (make sure start is top-left, end is bottom-right)
    left = min(start_x, end_x)
    top = min(start_y, end_y)
    right = max(start_x, end_x)
    bottom = max(start_y, end_y)
    
    # Crop the image using the specified coordinates
    cropped_img = img.crop((left, top, right, bottom))
    #cropped_img.show()  # To display the cropped image
    cropped_img.save("cropped_screenshot.png")  # Save the cropped screenshot

def main():
    # Take a full-screen screenshot
    full_screenshot = ImageGrab.grab()

    # Collect mouse events until released
    with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
        listener.join()

    # Once mouse listener is done, crop the screenshot
    if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
        crop_screenshot(full_screenshot, start_x, start_y, end_x, end_y)
    else:
        print("No area selected.")

if __name__ == "__main__":
    main()
