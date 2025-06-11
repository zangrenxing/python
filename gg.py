import os
import time
import random
# 点击元宝中心
# os.system('adb -s 192.168.1.3:5555 shell input tap 976 734')
# time.sleep(random.randint(10, 20))
for i in range(0, 10):
    # 点击去赚钱
    os.system('adb shell input tap 914 1815')
    time.sleep(15)
    # 点击领取奖励
    os.system('adb shell input tap 977 839')
    time.sleep(4)
    # 点X
    os.system('adb shell input tap 1000 75')
    time.sleep(5)
