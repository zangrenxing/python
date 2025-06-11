import os
import time
import random
for i in range(0, 20):
    # os.system('adb -s SQRNW17513001086 shell input tap 635 1760')
    
    # os.system('adb -s SQRNW17513001086 shell input tap 903 961')
    # os.system('adb -s SQRNW17513001086 shell input tap 903 761')
    # os.system('adb -s SQRNW17513001086 shell input tap 203 1421')
    
    os.system('adb -s SQRNW17513001086 shell input tap 900 1700')

    time.sleep(random.uniform(11, 12))
    for i in range(0, 2):
        os.system('adb -s SQRNW17513001086 shell input swipe 500 1768 500 300 400')
        time.sleep(random.randint(10,10))
    os.system('adb -s SQRNW17513001086 shell input swipe 500 1768 500 300 400')

    time.sleep(random.uniform(0.5, 1))
    # time.sleep(random.uniform(6, 7))
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))