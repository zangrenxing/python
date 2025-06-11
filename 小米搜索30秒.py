import os
import time
import random
for i in range(0, 4):
    #得体力搜索
    os.system('adb -s 79e8d0f8 shell input tap 950 1551')
    # os.system('adb -s 79e8d0f8 shell input tap 950 1751')
    
    #睡觉搜索
    # os.system('adb -s 79e8d0f8 shell input tap 267 390')   
    
    #签到 赚钱卡搜索
    # os.system('adb -s 79e8d0f8 shell input tap 867 1790')   

    # os.system('adb -s 79e8d0f8 shell input tap 950 151')
    time.sleep(random.uniform(0.5, 1))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input tap 535 1092')
    time.sleep(random.uniform(0.3, 0.4))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input tap 590 1521')
    time.sleep(random.uniform(0.1, 0.2))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input tap 590 1521')
    time.sleep(random.uniform(0.1, 0.2))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input tap 540 2114')
    time.sleep(random.uniform(0.2, 0.4))
    # time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input tap 940 292')
    # os.system('adb -s 79e8d0f8 shell input tap 176 541')
    time.sleep(random.uniform(1, 2))
    for i in range(0, 4):
        # os.system('adb shell input swipe 500 1600 500 300 300')
        os.system('adb -s 79e8d0f8 shell input swipe 500 1500 500 100 6000')
        time.sleep(random.randint(1,1))
    time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(0.3, 0.5))
    # time.sleep(random.uniform(1, 2))