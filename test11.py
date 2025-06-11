import pywinauto.mouse
import win32api
import pyautogui
from time import sleep
from PIL import Image
import pyautogui
import time

def custom_scroll(clicks, x=None, y=None):
    if x is None or y is None:
        x, y = win32api.GetCursorPos()  # 获取当前鼠标位置
    
    pywinauto.mouse.scroll((x, y), clicks)
 
# 使用示例
rs = custom_scroll(10000,1300,500)  # 向下滚动
print(rs)

im=pyautogui.screenshot()#截取整个屏幕
om=im.crop((986,463,1056,533))#根据截取的屏幕仅截取“带赞的手势图片”，可以用pyautogui.mouseInfo()获取图片的位置(284,416,302,438)
om.save("yilingwan.png")#将图片保存供pyautogui.locateOnScreen（）使用

 
sleep(3.5)  # 等待页面滚动
# pyautogui.scroll(-120)  # 向下滚动
# 初始化滚动条位置
# for i in range(0,12):
while True:
    pyautogui.scroll(-3)  # 向下滚动
