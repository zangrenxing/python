# from appium import webdriver
# from selenium.webdriver import ActionChains
# from lib2to3.pgen2 import driver
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# from ipywidgets.widgets import interaction
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(916, 300)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
    
# driver.back()

import pyautogui
import time
 
# # 移动鼠标到屏幕上的(x=100, y=100)位置
# pyautogui.moveTo(1343, 146, duration=1)
 
# # 等待1秒，以便观察移动结果
# time.sleep(1)
 
# # 点击鼠标左键
# pyautogui.click()
 
# # 等待1秒，以便观察点击结果
# time.sleep(1)
 
# # 移动鼠标到屏幕上的(x=200, y=200)位置
# pyautogui.moveTo(1070, 822, duration=1)
 
# # 等待1秒，以便观察移动结果
# time.sleep(1)
 
# # 点击鼠标右键
# pyautogui.click(button='right')

# 如果你想获取当前鼠标的位置，可以使用position()函数



# current_mouse_position = pyautogui.position()
# print(f"当前鼠标位置: {current_mouse_position}")



from pynput.mouse import Controller, Button

# 创建一个鼠标控制器
mouse = Controller()

# 模拟鼠标左键点击当前位置
mouse.click(Button.left, 1)

# 模拟在指定位置点击
# 需要注意的是，`pynput`使用的是屏幕上的绝对坐标
mouse.position = (100, 150)
mouse.click(Button.left, 1)

# 也可以模拟鼠标右键点击
mouse.click(Button.right, 1)

# 模拟鼠标中键点击
mouse.click(Button.middle, 1)

# 模拟鼠标双击
mouse.click(Button.left, 2)

# 模拟鼠标按下和释放
mouse.press(Button.left)
# 在这里，你可以执行一些其他的操作，如移动鼠标、等待等
mouse.release(Button.left)
