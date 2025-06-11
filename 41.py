import os
import time
import random
import pyautogui
for i in range(0, 50):
    # os.system('adb shell input swipe 500 1600 500 300 300')
    os.system('adb -s SQRNW17513001086 shell input tap 916 1166')
    # os.system('adb -s 79e8d0f8 shell input tap 916 1766')
    #os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 300')
    time.sleep(random.uniform(7, 8))
    # os.system('adb -s SQRNW17513001086 shell input tap 110 550')
    # time.sleep(random.uniform(1, 2))
    # pyautogui.press('f5')
    for i in range(0, 4):
        # os.system('adb shell input swipe 500 1600 500 300 300')
        # os.system('adb -s 79e8d0f8 shell input swipe 500 1500 500 100 6000')
        os.system('adb -s SQRNW17513001086 shell input swipe 500 1600 500 300 300')
        time.sleep(random.randint(4,6))
    time.sleep(random.uniform(2, 3))
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    time.sleep(random.uniform(4, 5))


