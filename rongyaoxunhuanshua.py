import os
import time
import random
for i in range(0, 2000):
    # os.system('adb shell input swipe 500 1600 500 300 300')
    os.system('adb -s 54L9X18323W13458 shell input swipe 500 1150 500 250 300')
    # time.sleep(1)
    time.sleep(random.randint(1, 3))
    os.system('adb -s 54L9X18323W13458 shell input swipe 500 300 500 1000 300')
    time.sleep(random.randint(1, 3))
