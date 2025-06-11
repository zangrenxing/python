import os
import time
import random
for i in range(0, 9):
    # os.system('adb shell input swipe 500 1600 500 300 300')
    # os.system('adb -s SQRNW17513001086 shell input swipe 500 1600 500 300 400')
    os.system('adb -s 79e8d0f8 shell input swipe 500 1600 500 300 300')

    # time.sleep(4)
    time.sleep(random.randint(10, 11))