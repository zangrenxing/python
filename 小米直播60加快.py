import os
import time
import random
for i in range(0, 20):
    os.system('adb -s 79e8d0f8 shell input tap 203 1621')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1700')
    # os.system('adb -s 79e8d0f8 shell input tap 635 1660')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1800')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1900')

    time.sleep(random.uniform(10, 11))
    for i in range(0, 2):
        os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 400')
        time.sleep(random.randint(10,10))
    os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 400')

    time.sleep(random.uniform(2, 3))
    # time.sleep(random.uniform(3, 4))
    # time.sleep(random.uniform(5, 6))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))