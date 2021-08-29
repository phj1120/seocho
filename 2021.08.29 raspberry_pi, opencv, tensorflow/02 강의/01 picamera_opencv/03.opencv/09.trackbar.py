import cv2


cv2.namedWindow("window")
cv2.createTrackbar("t1", "window", 0, 180, lambda x: x)
cv2.setTrackbarPos("t1", "window", 50)

cv2.waitKey(0)
cv2.destroyAllWindows()
