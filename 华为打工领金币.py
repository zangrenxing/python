import os
import time
import random
# for i in range(0, 50):
#     #点击去打工
#     os.system('adb -s SQRNW17513001086 shell input tap 552 1768') 
#     time.sleep(random.uniform(6, 7))
#     #点击领取元宝
#     os.system('adb -s SQRNW17513001086 shell input tap 529 1082') 
#     time.sleep(random.uniform(4, 5))
#     os.system('adb -s SQRNW17513001086 shell input keyevent 4')
#     time.sleep(random.uniform(4, 5))
#     #点击去打工
#     os.system('adb -s SQRNW17513001086 shell input tap 552 1768') 
#     time.sleep(random.uniform(6, 7))
#     #点击去打工赚钱
#     os.system('adb -s SQRNW17513001086 shell input tap 529 1082') 
#     time.sleep(random.uniform(4, 5))
#     #点击开始打工
#     os.system('adb -s SQRNW17513001086 shell input tap 545 1592') 
#     time.sleep(random.uniform(610, 615))

#     os.system('adb -s SQRNW17513001086 shell input keyevent 4')
#     time.sleep(random.uniform(3, 4))
    
for i in range(0, 50):
    #点击领取元宝
    os.system('adb -s SQRNW17513001086 shell input tap 529 1082') 
    time.sleep(random.uniform(4, 5))
    #点击返回
    os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    time.sleep(random.uniform(4, 5))
    #点击去打工
    os.system('adb -s SQRNW17513001086 shell input tap 552 1768') 
    time.sleep(random.uniform(6, 7))
    #点击去打工赚钱
    os.system('adb -s SQRNW17513001086 shell input tap 529 1082') 
    time.sleep(random.uniform(4, 5))
    #点击开始打工
    os.system('adb -s SQRNW17513001086 shell input tap 545 1592') 
    time.sleep(random.uniform(610, 615))

    # os.system('adb -s SQRNW17513001086 shell input keyevent 4')
    # time.sleep(random.uniform(3, 4))
    # #点击去打工
    # os.system('adb -s SQRNW17513001086 shell input tap 552 1768') 
    # time.sleep(random.uniform(6, 7))
