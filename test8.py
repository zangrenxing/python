
import pyautogui
 
# 找到图像的坐标，如果找到多个，默认点击第一个
# image_location = pyautogui.locateAllOnScreen(r"J:\xiaotu.png")
try:
    image_location = pyautogui.locateOnScreen("anquang.png", confidence=0.8)
    x, y = pyautogui.center(image_location)
    pyautogui.click(x, y)
    # if image_location:
    #     x, y = pyautogui.center(image_location)
    #     pyautogui.click(x, y)
    # else:
    #     print('图像未找到')
except:
    print('出错了，图像未找到')
    

    
