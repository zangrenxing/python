import os
import time
import random
for i in range(0, 2000):
    os.system('adb -s 79e8d0f8 shell input swipe 500 300 500 1000 300')
    time.sleep(random.randint(3, 7))
    os.system('adb -s 79e8d0f8 shell input swipe 500 1150 500 250 300')
    time.sleep(random.randint(3, 7))
