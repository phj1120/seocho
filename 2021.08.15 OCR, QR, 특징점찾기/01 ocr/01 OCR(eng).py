import cv2
import pytesseract

img = cv2.imread('img/english.png')
ocr = pytesseract.image_to_string(img)

print(ocr)