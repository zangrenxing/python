
import cv2
import pytesseract
 
def find_pattern(image_path):
    # 读取待搜索的图像
    image = cv2.imread(image_path)
 
    # 使用图像识别库进行图像识别和文字检测
    extracted_text = pytesseract.image_to_string(image)
    
    pattern = '特定图案'
    match_indices = [i for i, text in enumerate(extracted_text) if pattern in text]
 
    if len(match_indices) > 0:
        print(f"Pattern found at indices: {match_indices}")
        # 可以根据需求输出或显示匹配的结果
    else:
        print('Pattern not found.')
 
# 使用示例
find_pattern(r"J:\datu.png")