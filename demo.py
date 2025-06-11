from appium import webdriver
import time

desired_caps = dict()
desired_caps['platformName'] = 'Android' 
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = '79e8d0f8'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.MainSettings'

driver = webdriver.Remote('http://locahost:4723/wd/hub', desired_caps)
 
time.sleep(5)
driver.quit()
