import os
import time
import random
for i in range(0, 2000):
    # 点击领取
    os.system('adb -s A10ECMN2FTV9 shell input tap 960 316')
    time.sleep(2)
    # 领取后关弹窗
    os.system('adb -s A10ECMN2FTV9 shell input tap 954 204')
    time.sleep(1)
    # 上滑
    os.system('adb -s A10ECMN2FTV9 shell input swipe 900 1650 900 300 300')
    time.sleep(1)
    # 点击看直播
    os.system('adb -s A10ECMN2FTV9 shell input tap 900 960')
    time.sleep(2)

    for j in range(0, 4):
        # 点击金蛋
        time.sleep(150)
        os.system('adb -s A10ECMN2FTV9 shell input tap 980 740')

    time.sleep(600)

    # time.sleep(4)
    # os.system('adb -s 192.168.1.3:5555 shell input swipe 500 1600 500 300 300')
    # time.sleep(random.randint(3, 7))
    # os.system('adb shell input swipe 500 1600 500 300 300')
    # os.system('adb -s A10ECMN2FTV9 shell input swipe 500 1600 500 300 300')
    # time.sleep(4)
    # time.sleep(random.randint(3, 7))
    # 点击去赚钱
    # os.system('adb -s 192.168.1.3:5555 shell input tap 911 1822')
    # time.sleep(120)
    # 点击金蛋
    # os.system('adb -s 192.168.1.3:5555 shell input tap 984 738')
    # time.sleep(60)
    # 点击金蛋
    # os.system('adb -s 192.168.1.3:5555 shell input tap 984 738')
    # time.sleep(5)
    # 点击金蛋回元宝中心
    # os.system('adb -s 192.168.1.3:5555 shell input tap 984 738')
    # time.sleep(10)
    # 点头顶
    # os.system('adb -s 192.168.1.3:5555 shell input tap 951 211')
    # time.sleep(10)
    # 点头顶
    # os.system('adb -s 192.168.1.3:5555 shell input tap 951 211')
    # time.sleep(5)
    # 点击去赚钱
    # os.system('adb -s 192.168.1.3:5555 shell input tap 911 1822')
    # time.sleep(120)
