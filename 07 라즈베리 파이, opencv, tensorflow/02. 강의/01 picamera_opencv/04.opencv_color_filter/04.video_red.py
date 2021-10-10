import cv2
import numpy as np


lower = {
    "red": (170, 100, 100),
    "green": (50, 100, 100),
    "blue": (110, 100, 100),
    "yellow": (10, 100, 100)
}

upper = {
    "red": (180, 255, 255),
    "green": (70, 255, 255),
    "blue": (130, 255, 255),
    "yellow": (40, 255, 255)
}

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # red
    red = cv2.inRange(hsv, lower["red"], upper["red"])
    red = np.array(red)
    red = np.reshape(red, (240, 320,))
    mask = cv2.bitwise_and(img, img, mask=red)

    cv2.imshow("img", img)
    cv2.imshow("mask", mask)

    # press 'ESC' to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
