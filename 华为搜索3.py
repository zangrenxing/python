import os
import time
import random
for i in range(0, 4):
    # os.system('adb -s SQRNW17513001086 shell input tap 955 138')
    # os.system('adb -s SQRNW17513001086 shell input tap 555 1638')
    
    # 签到搜索
    os.system('adb -s SQRNW17513001086 shell input tap 860 1663')
    # 
    #睡觉搜索
    # os.system('adb -s SQRNW17513001086 shell input tap 169 580') 
    # time.sleep(random.uniform(0.5, 1))
    time.sleep(random.uniform(3, 4))
    os.system('adb -s SQRNW17513001086 shell input tap 550 1082')
    time.sleep(random.uniform(0.4, 0.6))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s SQRNW17513001086 shell input tap 587 1212')
    time.sleep(random.uniform(0.1, 0.2))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s SQRNW17513001086 shell input tap 590 1211')
    time.sleep(random.uniform(0.2, 0.4))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s SQRNW17513001086 shell input tap 650 1701')
    time.sleep(random.uniform(0.2, 0.4))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s SQRNW17513001086 shell input tap 952 286')
    # os.system('adb -s SQRNW17513001086 shell input tap 176 541')
    time.sleep(random.uniform(1, 2))
    for i in range(0, 6):
        # os.system('adb shell input swipe 500 1600 500 300 300')
        os.system('adb -s SQRNW17513001086 shell input swipe 500 1500 500 100 6000')
        time.sleep(random.randint(1,1))
    time.sleep(random.uniform(1, 2))
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    # time.sleep(random.uniform(3, 4))
    time.sleep(random.uniform(1, 2))