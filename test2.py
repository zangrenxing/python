
import cv2
# 读取图像文件
# image = cv2.imread("H:\py\DLLs\Lib\site-packages\cv2\demo.png", cv2.IMREAD_COLOR)
image = cv2.imread(r"J:\xiaotu.png", cv2.IMREAD_COLOR)
# image = cv2.imread("demo.jpg", cv2.IMREAD_COLOR)
# 检查图像是否成功读取
if image is not None:
    # 显示图像
    cv2.imshow('Image', image)
    # 等待按键按下后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
else:
    print("Failed to read the image.")
cv2.imwrite('xiaotu.png', image)