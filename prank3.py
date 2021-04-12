import time
import random
import pyautogui  #install the module, command: "pip install pyautogui"

def move_mouse(secs):
    start_time = time.time()
    elapsed_time = time.time() - start_time
    x_size, y_size = pyautogui.size()

    while elapsed_time < secs:
        x, y = random.randrange(x_size), random.randrange(y_size)
        pyautogui.moveTo(x, y, duration = 0.2)
        elapsed_time = time.time() - start_time


if __name__ == "__main__":
    pyautogui.alert("Your System Update is now completed.")
    move_mouse(120)
