import cv2
import numpy as np


img = cv2.imread("../images/circles.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# red circle
# blue, green, red => (36, 28, 237)
red = np.uint8([[[36, 28, 237]]])
red_hsv = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
red_hue = red_hsv[0][0][0]

# red
red_low = np.array([(red_hue - 10), 100, 100], dtype=np.uint8)
red_high = np.array([(red_hue + 10), 255, 255], dtype=np.uint8)
mask = cv2.inRange(img_hsv, red_low, red_high)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
