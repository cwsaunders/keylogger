from pynput.mouse import Listener

def appendtofile(x,y):
    print(f'Position: {x,y}')


with Listener(on_move=appendtofile) as l:
    l.join()