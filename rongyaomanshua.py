import os
import time
import random
for i in range(0, 2000):
    
    # os.system('adb shell input swipe 500 1600 500 300 300')
    # os.system('adb -s 54L9X18323W13458 shell input swipe 500 1300 500 100 6000')
    # os.system('adb -s 192.168.31.132:5555 shell input swipe 500 random.randint(1100,1200) 500 random.randint(50,150) 6000')

    cmd = fr'adb -s 54L9X18323W13458 shell input swipe {random.randint(150,550)} {random.randint(1100,1200)} {random.randint(150,550)} {random.randint(50,150)} {random.randint(6000,7000)}'
    # cmd = fr'adb -s 192.168.31.132:5555 shell input swipe {random.randint(150,550)} {random.randint(1100,1200)} {random.randint(150,550)} {random.randint(50,150)} {random.randint(6000,7000)}'
    # os.system('adb -s 192.168.31.132:5555 shell input swipe ' + str(random.randint(150,550)) + ' ' + str(random.randint(1100,1200)) + ' ' + str(random.randint(150,550)) + ' ' + str(random.randint(50,150)) + ' '  + str(random.randint(4000,6000)))
    os.system(cmd)

    # os.system('adb -s 192.168.31.132:5555 shell input swipe ' + str(random.randint(150,550)) + ' ' + str(random.randint(1100,1200)) + ' ' + str(random.randint(150,550)) + ' ' + str(random.randint(50,150)) + ' '  + str(random.randint(4000,6000)))
    # os.system('adb -s 192.168.31.132:5555 shell input swipe 500 ' + str(random.randint(1100,1200)) + ' ' + str(500) + ' ' + str(random.randint(50,150)) + ' '  + str(6000))
    # os.system('adb -s 192.168.31.132:5555 shell input swipe 500 1200 500 100 6000')
    # time.sleep(4)
    # time.sleep(random.uniform(0,1))
    # time.sleep(random.randint(1,1))