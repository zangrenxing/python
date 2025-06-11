import os
import time
import random
import pyautogui
for i in range(0, 20):
    # os.system('adb -s 79e8d0f8 shell input tap 528 1988')
    # os.system('adb -s 79e8d0f8 shell input tap 528 1788')
    # os.system('adb -s 79e8d0f8 shell input tap 501 1559')
    
    # os.system('adb -s 79e8d0f8 shell input tap 900 1400')
    #平华为底
    # os.system('adb -s 79e8d0f8 shell input tap 900 1700')
    
    # 倒数第二排
    os.system('adb -s 79e8d0f8 shell input tap 202 2097')
    # os.system('adb -s 79e8d0f8 shell input tap 800 2137')
    
    #os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 300')
    time.sleep(random.uniform(2, 3))
    # os.system('adb -s SQRNW17513001086 shell input tap 110 550')
    # time.sleep(random.uniform(1, 2))
    # pyautogui.press('f5')
    for i in range(0, 4):
        # os.system('adb shell input swipe 500 1600 500 300 300')
        os.system('adb -s 79e8d0f8 shell input swipe 500 1800 500 300 6000')
        # os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 300')
        time.sleep(random.randint(1,2))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(3, 4))


