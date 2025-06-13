import os
import time
import random
for i in range(0, 2000):
    # os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 300')
    os.system('adb -s 79e8d0f8 shell input swipe 500 1000 500 300 300')
    # time.sleep(random.randint(8, 9))
    time.sleep(random.randint(8, 19))
