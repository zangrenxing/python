import os
import time
import random
# 点击元宝中心
# os.system('adb -s 192.168.1.3:5555 shell input tap 976 734')
# time.sleep(random.randint(10, 20))
for i in range(0, 10):
    # 点击看直播
    os.system('adb shell input tap 312 306')
    time.sleep(100)
    # 点X
    os.system('adb shell input tap 1010 128')
    time.sleep(5)

