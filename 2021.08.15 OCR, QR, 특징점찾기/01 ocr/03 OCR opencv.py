import pytesseract
import cv2
import os

filename = "img/example_02.png"
image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

gray = cv2.medianBlur(gray, 3)

text = pytesseract.image_to_string(gray)
print(text)

cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)