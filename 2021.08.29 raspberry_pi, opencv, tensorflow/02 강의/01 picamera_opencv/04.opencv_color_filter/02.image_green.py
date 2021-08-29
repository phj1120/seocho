import cv2
import numpy as np


img = cv2.imread("../images/circles.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# green circle
# blue, green, red => (76, 177, 34)
green = np.uint8([[[76, 177, 34]]])
green_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
green_hue = green_hsv[0][0][0]

# red
green_low = np.array([(green_hue - 10), 100, 100], dtype=np.uint8)
green_high = np.array([(green_hue + 10), 255, 255], dtype=np.uint8)
mask = cv2.inRange(img_hsv, green_low, green_high)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
