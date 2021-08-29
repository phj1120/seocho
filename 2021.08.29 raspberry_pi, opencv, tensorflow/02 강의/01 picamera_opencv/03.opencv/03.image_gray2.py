import cv2


img = cv2.imread("../images/cat.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.imread("../images/cat.jpg", 0)

cv2.imshow("gray", gray)
cv2.imshow("gray2", gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()
