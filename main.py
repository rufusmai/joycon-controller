import signal
import readchar
import time
from pynput.mouse import Button, Controller
from pyjoycon import GyroTrackingJoyCon, ButtonEventJoyCon, get_R_id


class ControllerJoyCon(
    GyroTrackingJoyCon,
    ButtonEventJoyCon
): pass


def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)  # clear the printed line
        print("    ", end="\r", flush=True)


signal.signal(signal.SIGINT, handler)

joycon_id = get_R_id()
joycon = ControllerJoyCon(*joycon_id)
mouse = Controller()

while True:
    time.sleep(0.05)

    for event_type, status in joycon.events():
        if status:
            if event_type == 'a':
                print('leftclick')
                mouse.press(Button.left)
            elif event_type == 'b':
                print('rightclick')
                mouse.press(Button.right)

