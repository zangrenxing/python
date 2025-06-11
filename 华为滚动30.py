import os
import time
import random
for i in range(0, 20):
    # os.system('adb -s SQRNW17513001086 shell input tap 841 747')
    # os.system('adb -s SQRNW17513001086 shell input tap 841 947')
    # os.system('adb -s SQRNW17513001086 shell input tap 910 1266')
    os.system('adb -s SQRNW17513001086 shell input tap 916 1666')
    # os.system('adb -s SQRNW17513001086 shell input tap 916 1466')
    time.sleep(random.uniform(5, 6))
    for i in range(0, 7):
        os.system('adb -s SQRNW17513001086 shell input swipe 500 1600 500 300 300')
        time.sleep(random.randint(3, 4))
    # time.sleep(random.uniform(1, 1.3))
    # time.sleep(random.uniform(0.5, 1))

    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))
    # time.sleep(random.uniform(5, 6))

