import pyautogui

#获取鼠标信息

info = pyautogui.mouseInfo()

# print(f"Mouse position: {info.x}, {info.y}")
# print(f"Screen resolution: {info.width} x {info.height}")
# print(f"DPI: {info.dpi}")

im=pyautogui.screenshot()#截取整个屏幕
om=im.crop((387,245,454,306))#根据截取的屏幕仅截取“带赞的手势图片”，可以用pyautogui.mouseInfo()获取图片的位置(284,416,302,438)
# om=im.crop((1123,537,1247,720))#根据截取的屏幕仅截取“带赞的手势图片”，可以用pyautogui.mouseInfo()获取图片的位置(284,416,302,438)
om.save("anquang.png")#将图片保存供pyautogui.locateOnScreen（）使用
# om.save("qudagong.png")#将图片保存供pyautogui.locateOnScreen（）使用
