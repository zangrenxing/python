import os
import time
import random
import pyautogui
for i in range(0, 13):
    # os.system('adb -s 79e8d0f8 shell input tap 818 1400')
    # os.system('adb -s 79e8d0f8 shell input tap 921 1235')
    # os.system('adb -s 79e8d0f8 shell input tap 672 1581')
    # os.system('adb -s 79e8d0f8 shell input tap 200 1800')
    # os.system('adb -s 79e8d0f8 shell input tap 200 1900')
    # os.system('adb -s 79e8d0f8 shell input tap 200 2100')
    os.system('adb -s 79e8d0f8 shell input tap 911 1159')

    time.sleep(random.uniform(182, 184))
    # time.sleep(random.uniform(62, 64))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))
    time.sleep(random.uniform(4, 5))

