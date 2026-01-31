
# 자동 스크린샷

import time
from PIL import ImageGrab

time.sleep(10)

for i in range(1,11):
    img = ImageGrab.grab()
    img.save(f"image{i}.png")
    time.sleep(5)
