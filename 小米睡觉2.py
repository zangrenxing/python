import os
import time
import random
for i in range(0, 4):   
    os.system('adb -s 79e8d0f8 shell input tap 167 590')   
    # os.system('adb -s 79e8d0f8 shell input tap 267 390')   
    time.sleep(random.uniform(1, 2))
    for i in range(0, 8):
        os.system('adb -s 79e8d0f8 shell input swipe 500 1800 500 300 6000')
        time.sleep(random.randint(1,1))
    time.sleep(random.uniform(1, 2))
    os.system('adb -s 79e8d0f8 shell input keyevent 4')
    time.sleep(random.uniform(1, 1.5))
    

# os.system('adb -s 79e8d0f8 shell input tap 167 590')   
# time.sleep(random.uniform(1, 2))
# for i in range(0, 6):   
#     os.system('adb -s 79e8d0f8 shell input tap 167 590')   
#     time.sleep(random.uniform(31, 32))
#     os.system('adb -s 79e8d0f8 shell input keyevent 4')
#     time.sleep(random.uniform(0.8, 1))
#     time.sleep(random.uniform(1, 1.5))


