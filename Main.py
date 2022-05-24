import time
import random
import win32api
import keyboard


toggle_button: str = "E"
times: int = 0.001
pos: int = 60
enabled: bool = False


def is_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0


print(f"起動{toggle_button}でON/OFF切り替え")
if enabled:
    print("初期:有効")
else:
    print("初期:無効")
last_state: bool = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("有効")
            else:
                print("無効")
    if is_mouse_down() and enabled:
        for i in [
            [-pos, 0],
            [0, pos],
            [pos, 0],
            [0, -pos],
        ]:
            win32api.mouse_event(0x0001, i[0], i[1])
            time.sleep(times)
    time.sleep(random.choice([0.01, 0.02]))
