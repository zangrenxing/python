import os
import time
import random
# 点击元宝中心
# os.system('adb -s A10ECMN2FTV9 shell input tap 976 734')
# time.sleep(random.randint(10, 20))
for i in range(0, 2000):
    # 点击去赚钱
    # os.system('adb -s A10ECMN2FTV9 shell input tap 911 1822')
    # time.sleep(120)
    # 点击金蛋
    # os.system('adb -s A10ECMN2FTV9 shell input tap 984 738')
    # time.sleep(60)
    # 点击金蛋
    # os.system('adb -s A10ECMN2FTV9 shell input tap 984 738')
    # time.sleep(5)
    # 点击金蛋回元宝中心
    os.system('adb -s A10ECMN2FTV9 shell input tap 984 738')
    time.sleep(10)
    # 点头顶
    os.system('adb -s A10ECMN2FTV9 shell input tap 951 211')
    time.sleep(10)
    # 点头顶
    os.system('adb -s A10ECMN2FTV9 shell input tap 951 211')
    time.sleep(5)
    # 点击去赚钱
    os.system('adb -s A10ECMN2FTV9 shell input tap 911 1822')
    time.sleep(120)

    # time.sleep(4)
    # os.system('adb -s A10ECMN2FTV9 shell input swipe 500 1600 500 300 300')
    # time.sleep(random.randint(3, 7))
