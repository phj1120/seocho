import cv2


img = cv2.imread("../images/cat.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("../images/gray.jpg", gray)
