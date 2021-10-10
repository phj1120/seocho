import cv2
import pytesseract

img = cv2.imread('img/korean.png')
ocr = pytesseract.image_to_string(img, lang='kor')

print(ocr)