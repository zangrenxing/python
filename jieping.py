import pyautogui

im=pyautogui.screenshot()#截取整个屏幕
im.save("jiequangping.png")#将图片保存供pyautogui.locateOnScreen（）使用
