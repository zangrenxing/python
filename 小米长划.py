import os
import time
import random
for i in range(0, 100):
    os.system('adb -s 79e8d0f8 shell input swipe 500 1800 500 300 6000')
    # time.sleep(random.randint(1, 2))