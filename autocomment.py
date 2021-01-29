import pyautogui
import time
time.sleep(2)

for i in range(100):
    pyautogui.write(".")
    pyautogui.press("Enter")
    time.sleep(2)