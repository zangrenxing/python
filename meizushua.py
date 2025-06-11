import os
import time
import random
for i in range(0, 2000):
    # os.system('adb -s 79e8d0f8 shell input swipe 500 300 500 1000 300')
    # time.sleep(random.randint(3, 7))
    # os.system('adb shell input swipe 500 1600 500 300 300')
    os.system('adb -s A10ECMN2FTV9 shell input swipe 500 1600 500 300 300')
    # os.system('adb -s 192.168.31.52:5555 shell input swipe 500 1600 500 300 300')
    # time.sleep(4)
    time.sleep(random.randint(3, 7))