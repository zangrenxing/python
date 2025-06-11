import os
import time
import random
import pyautogui 
for i in range(0, 20):
    # os.system('adb -s 79e8d0f8 shell input tap 203 1521')
    os.system('adb -s 79e8d0f8 shell input tap 635 1660')
    
    # os.system('adb -s 79e8d0f8 shell input tap 900 2000')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1900')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1800')
    # 
    # os.system('adb -s 79e8d0f8 shell input tap 900 1600')

    time.sleep(random.uniform(11, 12))
    for i in range(0, 8):
        os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 400')
        time.sleep(random.randint(10,10))
    os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 400')

    # time.sleep(random.uniform(2, 3))
    time.sleep(random.uniform(3, 4))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(5, 6))
    # time.sleep(random.uniform(1, 2))