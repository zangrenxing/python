import os
import time
import random
for i in range(0, 5):   
    os.system('adb -s SQRNW17513001086 shell input tap 260 403')   
    # os.system('adb -s SQRNW17513001086 shell input tap 160 603')   
    time.sleep(random.uniform(1, 2))
    for i in range(0, 8):
        os.system('adb -s SQRNW17513001086 shell input swipe 500 1500 500 100 6000')
        time.sleep(random.randint(1,1))
    time.sleep(random.uniform(1, 2)) 
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    time.sleep(random.uniform(3, 4))
    
os.system('adb -s SQRNW17513001086 shell input tap 260 403')   
# os.system('adb -s SQRNW17513001086 shell input tap 160 603')   
time.sleep(random.uniform(1, 2))
for i in range(0, 9):
    os.system('adb -s SQRNW17513001086 shell input swipe 500 1500 500 100 6000')
    time.sleep(random.randint(1,1))
# time.sleep(random.uniform(4, 5)) 
time.sleep(random.uniform(1, 2)) 
os.system('adb -s SQRNW17513001086 shell input keyevent 4')
