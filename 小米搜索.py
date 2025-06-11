import os
import time
import random
import pyautogui
for i in range(0, 20):
    # os.system('adb -s 79e8d0f8 shell input tap 950 1780')
    os.system('adb -s 79e8d0f8 shell input tap 950 140')
    #os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 300')
    time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input tap 176 541')
    time.sleep(random.uniform(1, 2))
    for i in range(0, 6):
        # os.system('adb shell input swipe 500 1600 500 300 300')
        os.system('adb -s 79e8d0f8 shell input swipe 500 1500 500 100 6000')
        time.sleep(random.randint(1,1))
    time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))


