import os
import time
import random

# 模拟真人滑动手机屏幕
def human_swipe(device_id, max_seconds=30):
    start_time = time.time()
    swipe_count = 0
    while True:
        # 检查是否超过最大运行时长
        if time.time() - start_time > max_seconds:
            break

        # 随机起点和终点，模拟不同手势
        start_x = random.randint(400, 600)
        start_y = random.randint(1600, 2000)
        end_x = start_x + random.randint(-50, 50)
        end_y = random.randint(300, 600)
        duration = random.randint(800, 1800)  # 毫秒

        cmd = f'adb -s {device_id} shell input swipe {start_x} {start_y} {end_x} {end_y} {duration}'
        os.system(cmd)

        # 随机停顿，模拟人手操作
        # time.sleep(random.uniform(1, 2.5))
        swipe_count += 1

    print(f"已运行{max_seconds}秒，共滑动{swipe_count}次。")

if __name__ == "__main__":
    device_id = "79e8d0f8"  # 替换为你的设备ID
    human_swipe(device_id, max_seconds=190)  # 30分钟