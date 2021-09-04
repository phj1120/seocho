import cv2
import numpy as np


img = cv2.imread("../images/circles.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# blue circle
# blue, green, red => (204, 72, 63)
blue = np.uint8([[[204, 72, 63]]])
blue_hsv = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
blue_hue = blue_hsv[0][0][0]

# red
blue_low = np.array([(blue_hue - 10), 100, 100], dtype=np.uint8)
blue_high = np.array([(blue_hue + 10), 255, 255], dtype=np.uint8)
mask = cv2.inRange(img_hsv, blue_low, blue_high)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
