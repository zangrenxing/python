import os
import time
import random
import threading

# 为线程定义一个函数
def lq():
    for i in range(0, 2000):
        # 点击领取
        os.system('adb -s A10ECMN2FTV9 shell input tap 960 316')
        time.sleep(2)
        # 领取后关弹窗
        os.system('adb -s A10ECMN2FTV9 shell input tap 954 204')
        time.sleep(1)
        # 上滑
        os.system('adb -s A10ECMN2FTV9 shell input swipe 900 1650 900 300 300')
        time.sleep(1)
        # 点击看直播
        os.system('adb -s A10ECMN2FTV9 shell input tap 900 960')
        time.sleep(2)
        threading.Thread.start(yb())
        time.sleep(600)
        # 点击X
        os.system('adb -s A10ECMN2FTV9 shell input tap 997 98')
        time.sleep(2)

def yb():
    for j in range(0, 5):
        # 点击金蛋
        time.sleep(140)
        os.system('adb -s A10ECMN2FTV9 shell input tap 980 740')
    
    

# 创建两个线程
try:
   threading.Thread.start(lq())
except:
   print ("Error: 无法启动线程")
   print ("\a")

time.sleep(3600)
        
        
