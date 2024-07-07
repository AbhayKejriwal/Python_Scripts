from pynput import mouse

# File to save the recorded positions
output_file = "continuous_mouse_clicks.txt"

# Variable to store the last click position
last_click_position = None
# Variable to count consecutive clicks at the same position
click_count = 0

# Function to store mouse click events
def on_click(x, y, button, pressed):
    global last_click_position, click_count

    if pressed:
        current_position = (x, y)
        
        if current_position == last_click_position:
            click_count += 1
        else:
            last_click_position = current_position
            click_count = 1

        if click_count == 3:
            with open(output_file, "a") as f:
                f.write(f"{x}, {y}\n")
            click_count = 0  # Reset count after recording

# Start listening to mouse click events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
