import os
import time
import random
for i in range(0, 100):
    # os.system('adb shell input swipe 500 1600 500 300 300')
    os.system('adb -s SQRNW17513001086 shell input swipe 500 1500 500 100 6000')
    # time.sleep(4)
    time.sleep(random.randint(1,1))
 