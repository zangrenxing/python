
import cv2
 
def find_pattern(image_path, pattern_path):
    # 读取待搜索的图像和目标图像
    image = cv2.imread(image_path)
    pattern = cv2.imread(pattern_path)
 
    # 使用模板匹配
    result = cv2.matchTemplate(image, pattern, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
 
    # 设置匹配阈值，可以根据实际情况调整
    threshold = 0.8
 
    # 找到最佳匹配位置的坐标
    if max_val >= threshold:
        top_left = max_loc
        bottom_right = (top_left[0] + pattern.shape[1], top_left[1] + pattern.shape[0])
        
        # 在原始图像上绘制矩形框来突出显示匹配出的图案
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.imshow('Matched Result', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('Pattern not found.')
 
# 使用示例
find_pattern("J:/datu.png", "J:/xiaotu.png")
# find_pattern(r"J:\datu.png", r"J:\xiaotu.png")