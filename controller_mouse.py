from pynput.mouse import Controller


# Mouse movement function
def control_mouse():
    mouse = Controller()
    mouse.position = (10,20)

