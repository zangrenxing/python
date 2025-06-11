# import pyautogui
 
# x, y = pyautogui.size()  # 当前屏幕分辨率的大小 (x,y)
# print("screen_size: ", x, "*", y)
# pyautogui.alert(text='', title='', button='')
# text = pyautogui.alert(text='你好呀', title='消息框', button='ok')
# print(text)

from PIL import Image
import pyautogui
import time
# im=pyautogui.screenshot()#截取整个屏幕
# om=im.crop((986,463,1056,533))#根据截取的屏幕仅截取“带赞的手势图片”，可以用pyautogui.mouseInfo()获取图片的位置(284,416,302,438)
# om.save("yilingwan.png")#将图片保存供pyautogui.locateOnScreen（）使用

import pyautogui
from time import sleep
 
sleep(3.5)  # 等待页面滚动
# pyautogui.scroll(-120)  # 向下滚动
# 初始化滚动条位置
# for i in range(0,12):
while True:
    pyautogui.scroll(-3)  # 向下滚动
    

