
import keyboard

# Define the target string
target_string = "helloworld"

# Initialize a counter to track the position in the target string
position = 0

# Define a function that processes each key press
def on_key_event(event):
    global position
    if position < len(target_string):
        print(target_string[position], end="", flush=True)
        position += 1
    # Stop capturing once the target string is fully typed
    if position == len(target_string):
        keyboard.unhook_all()

# Hook the key press event to the function
keyboard.on_press(on_key_event,suppress=True)

# Block until all keys are pressed
keyboard.wait()
