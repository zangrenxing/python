import os
import time
import random
import pyautogui
for i in range(0, 30):
    #今日签到右下
    # os.system('adb -s SQRNW17513001086 shell input tap 216 1266')
    
    # os.system('adb -s SQRNW17513001086 shell input tap 503 1421')
    os.system('adb -s SQRNW17513001086 shell input tap 516 1666')
    time.sleep(random.uniform(1, 2))
    for i in range(0, 4):
        os.system('adb -s SQRNW17513001086 shell input swipe 500 1500 500 100 6000')
        time.sleep(random.randint(1,1))
    time.sleep(random.uniform(4, 5))
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))
    time.sleep(random.uniform(4, 5))


