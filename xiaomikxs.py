import os
import time
import random
for i in range(0, 2000):
    # os.system('adb shell input swipe 500 1600 500 300 300')
    # os.system('adb -s 54L9X18323W13458 shell input swipe 700 500 50 800 1000')
    # cmd = fr'adb -s SQRNW17513001086 shell input swipe {random.randint(600,700)} {random.randint(500,1000)} {random.randint(50,150)} {random.randint(500,1000)} {random.randint(700,1200)}'
    # cmd = fr'adb -s 54L9X18323W13458 shell input swipe {random.randint(600,700)} {random.randint(500,1000)} {random.randint(50,150)} {random.randint(500,1000)} {random.randint(700,1200)}'
    cmd = fr'adb -s 79e8d0f8 shell input swipe {random.randint(600,700)} {random.randint(500,1000)} {random.randint(50,150)} {random.randint(500,1000)} {random.randint(700,1200)}'
    # cmd = fr'adb -s 192.168.31.132:5555 shell input swipe {random.randint(600,700)} {random.randint(500,1000)} {random.randint(50,150)} {random.randint(500,1000)} {random.randint(700,1200)}'
    # os.system('adb -s 192.168.31.132:5555 shell input swipe ' + str(random.randint(150,550)) + ' ' + str(random.randint(1100,1200)) + ' ' + str(random.randint(150,550)) + ' ' + str(random.randint(50,150)) + ' '  + str(random.randint(4000,6000)))
    os.system(cmd)
    # cmd = fr'adb -s 192.168.31.132:5555 shell input swipe {random.randint(150,550)} {random.randint(1100,1200)} {random.randint(150,550)} {random.randint(50,150)} {random.randint(4000,6000)}'
    # # os.system('adb -s 192.168.31.132:5555 shell input swipe ' + str(random.randint(150,550)) + ' ' + str(random.randint(1100,1200)) + ' ' + str(random.randint(150,550)) + ' ' + str(random.randint(50,150)) + ' '  + str(random.randint(4000,6000)))
    # os.system(cmd)

    # time.sleep(4)
    time.sleep(random.randint(5,10))