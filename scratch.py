import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE = False
while(True):
    time.sleep(60)
    i = 0
    while i <= 5:
        pyautogui.press("insert")
        time.sleep(1)
        i += 1

    print("Logged successfully at {}".format(datetime.now().time()))
