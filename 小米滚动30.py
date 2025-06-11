import os
import time
import random
for i in range(0, 10):
    # 打工第三行看精彩30秒
    os.system('adb -s 79e8d0f8 shell input tap 915 1555')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1400')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1200')
    # os.system('adb -s 79e8d0f8 shell input tap 635 1660')
    # os.system('adb -s 79e8d0f8 shell input tap 900 1800')
    # os.system('adb -s 79e8d0f8 shell input tap 900 2100')
    # os.system('adb -s 79e8d0f8 shell input tap 921 1135')

    
    time.sleep(random.uniform(3, 4))
    for i in range(0, 4):
        os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 300')
        time.sleep(random.randint(6,7))
    time.sleep(random.uniform(2, 3))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))
    # time.sleep(random.uniform(4, 5))
