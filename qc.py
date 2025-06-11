import os
import time
import random
for i in range(0, 2000):
    # os.system('adb shell input swipe 500 1600 500 300 300')
    os.system('adb -s SQRNW17513001086 shell input swipe 500 1700 500 400 300')
    time.sleep(random.uniform(0.5, 1))
    os.system('adb -s SQRNW17513001086 shell input swipe 500 400 500 1700 300')
    # time.sleep(random.uniform(2, 3))
