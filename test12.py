import pyautogui
import win32api
import pywinauto
from time import sleep
from PIL import Image

# def custom_scroll(clicks, x=None, y=None):
#     if x is None or y is None:
#         x, y = win32api.GetCursorPos()  # 获取当前鼠标位置
#     pywinauto.mouse.scroll((x, y), clicks)
 
# # 使用示例
# rs = custom_scroll(-100,1300,500)  # 向下滚动
# print(rs)

# im=pyautogui.screenshot()#截取整个屏幕
# om=im.crop((986,463,1056,533))#根据截取的屏幕仅截取“带赞的手势图片”，可以用pyautogui.mouseInfo()获取图片的位置(284,416,302,438)
# om.save("yilingwan.png")#将图片保存供pyautogui.locateOnScreen（）使用

def ztdj(xiaotu):
    def custom_scroll(clicks, x=None, y=None):
        if x is None or y is None:
            x, y = win32api.GetCursorPos()  # 获取当前鼠标位置
        pywinauto.mouse.scroll((x, y), clicks)

    # 找到图像的坐标，如果找到多个，默认点击第一个
    c = 10
    while True:
        try:
            image_location = pyautogui.locateOnScreen(xiaotu, confidence=0.8)
            print(image_location)
            x, y = pyautogui.center(image_location)
            pyautogui.click(x, y)
            break
        except:
            print('未找到',xiaotu,'图,向下滚动')    
            custom_scroll(-1,1300,500)  # 向下滚动
            c -= 1

ztdj('qudagong.png')
    