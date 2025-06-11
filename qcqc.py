import os
import time
import random

#滑动30秒
# for i in range(0, 50):
#     #今日签到右下
#     # os.system('adb -s 192.168.31.142:5555 shell input tap 216 1266')
    
#     # os.system('adb -s 192.168.31.142:5555 shell input tap 503 1421')
#     # os.system('adb -s 192.168.31.142:5555 shell input tap 516 1666')
    
#     os.system('adb -s 192.168.31.142:5555 shell input tap 516 1666')
#     time.sleep(random.uniform(1, 2))
#     for i in range(0, 4):
#         os.system('adb -s 192.168.31.142:5555 shell input swipe 500 1500 500 100 6000')
#         time.sleep(random.randint(1,1))
#     # time.sleep(random.uniform(1, 2))
#     time.sleep(random.uniform(2, 3))
#     os.system('adb -s 192.168.31.142:5555 shell input keyevent 4')
#     time.sleep(random.uniform(1, 2))
#     # time.sleep(random.uniform(4, 5))
    
#得体力搜索30秒
# for i in range(0, 4):    
#     os.system('adb -s 192.168.31.142:5555 shell input tap 860 1663') 
#     time.sleep(random.uniform(3, 4))
#     os.system('adb -s 192.168.31.142:5555 shell input tap 550 1082')
#     time.sleep(random.uniform(0.4, 0.6))
#     # time.sleep(random.uniform(1, 2))
#     os.system('adb -s 192.168.31.142:5555 shell input tap 587 1212')
#     time.sleep(random.uniform(0.1, 0.2))
#     # time.sleep(random.uniform(1, 2))
#     os.system('adb -s 192.168.31.142:5555 shell input tap 590 1211')
#     time.sleep(random.uniform(0.2, 0.4))
#     # time.sleep(random.uniform(1, 2))
#     os.system('adb -s 192.168.31.142:5555 shell input tap 650 1701')
#     time.sleep(random.uniform(0.2, 0.4))
#     # time.sleep(random.uniform(1, 2))
#     os.system('adb -s 192.168.31.142:5555 shell input tap 952 286')
#     # os.system('adb -s 192.168.31.142:5555 shell input tap 176 541')
#     time.sleep(random.uniform(1, 2))
#     for i in range(0, 4):
#         # os.system('adb shell input swipe 500 1600 500 300 300')
#         os.system('adb -s 192.168.31.142:5555 shell input swipe 500 1500 500 100 6000')
#         time.sleep(random.randint(1,1))
#     time.sleep(random.uniform(1, 2))
#     os.system('adb -s 192.168.31.142:5555 shell input keyevent 4')
#     # time.sleep(random.uniform(3, 4))
#     time.sleep(random.uniform(1, 2))


#睡觉3
# for i in range(0, 4):   
#     os.system('adb -s 192.168.31.142:5555 shell input tap 165 581')   
#     time.sleep(random.uniform(1, 2))
#     for i in range(0, 8):
#         os.system('adb -s 192.168.31.142:5555 shell input swipe 500 1500 500 100 6000')
#         time.sleep(random.randint(1,1))
#     time.sleep(random.uniform(1, 2))
#     os.system('adb -s 192.168.31.142:5555 shell input keyevent 4')
#     time.sleep(random.uniform(3, 4))


#滚动30秒
def 滚动30秒 () :
    for i in range(0, 30):
        os.system('adb -s 192.168.31.142:5555 shell input tap 916 1666')
    time.sleep(random.uniform(5, 6))
    for i in range(0, 5):
        os.system('adb -s 192.168.31.142:5555 shell input swipe 500 1600 500 300 300')
        time.sleep(random.randint(4, 5))
    # time.sleep(random.uniform(4, 5))
    time.sleep(random.uniform(0.5, 1))
    os.system('adb -s 192.168.31.142:5555 shell input keyevent 4')
    time.sleep(random.uniform(1, 2))
    # time.sleep(random.uniform(5, 6))




def 直播3分钟加快 () :
    for i in range(0, 20):
        os.system('adb -s 192.168.31.142:5555 shell input tap 635 1760')
    time.sleep(random.uniform(11, 12))
    for i in range(0, 8):
        os.system('adb -s 192.168.31.142:5555 shell input swipe 500 1768 500 300 400')
        time.sleep(random.randint(10,10))
    os.system('adb -s 192.168.31.142:5555 shell input swipe 500 1768 500 300 400')
    # time.sleep(random.uniform(1, 2))
    time.sleep(random.uniform(4, 5))
    os.system('adb -s 192.168.31.142:5555 shell input keyevent 4')
    time.sleep(random.uniform(3, 4))
    # time.sleep(random.uniform(5, 6))
    # time.sleep(random.uniform(1, 2))

#直播3分钟加快
# 直播3分钟加快 ()
def a():
    # return
a()    
滚动30秒 ()