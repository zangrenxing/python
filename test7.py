import cv2
import numpy as np
#加载图片和图标
image = cv2.imread(r"J:\datu.png")
icon = cv2.imread(r"J:\xiaotu.png")
#执行模板匹配
result = cv2.matchTemplate(image,icon,cv2.TM_CCOEFF_NORMED)
print(result)