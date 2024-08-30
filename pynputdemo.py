
from pynput import keyboard

# The string to type instead of the user's input
replacement_string = "hello world"
index = 0  

def on_press(key):
    global index
    try:
        # Intercept any key press and type the next character of the replacement string
        if key.char!= replacement_string[index]:
            keyboard.Controller().press(replacement_string[index])
            keyboard.Controller().release(replacement_string[index])
            index += 1

    except AttributeError:
        pass

def on_release(key):
    # Stop the listener if ESC is pressed
    if key == keyboard.Key.esc:
        return False

def on_activate_h():
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h,
        '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()


# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release,suppress=True) as listener:
    listener.join()
