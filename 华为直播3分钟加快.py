import os
import time
import random
import pyautogui
for i in range(0, 20):
    # os.system('adb -s SQRNW17513001086 shell input tap 635 1760')
    # os.system('adb -s SQRNW17513001086 shell input tap 635 1260')
    
    # os.system('adb -s SQRNW17513001086 shell input tap 903 761')
    # os.system('adb -s SQRNW17513001086 shell input tap 203 1421')
    
    os.system('adb -s SQRNW17513001086 shell input tap 900 1700')

    time.sleep(random.uniform(11, 12))
    for i in range(0, 8):
        os.system('adb -s SQRNW17513001086 shell input swipe 500 1768 500 300 400')
        time.sleep(random.randint(10,10))
    os.system('adb -s SQRNW17513001086 shell input swipe 500 1768 500 300 400')

    # time.sleep(random.uniform(1, 2))
    time.sleep(random.uniform(4, 5))
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    time.sleep(random.uniform(3, 4))
    # time.sleep(random.uniform(5, 6))
    # time.sleep(random.uniform(1, 2))