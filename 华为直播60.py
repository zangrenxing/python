import os
import time
import random
import pyautogui
for i in range(0, 20):
    # os.system('adb -s SQRNW17513001086 shell input tap 914 1765')
    # os.system('adb -s SQRNW17513001086 shell input tap 914 765')
    os.system('adb -s SQRNW17513001086 shell input tap 223 1660')
    # time.sleep(random.uniform(62, 64))
    time.sleep(random.uniform(65, 66))
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    # time.sleep(random.uniform(4, 5))
    time.sleep(random.uniform(0.5, 1))

