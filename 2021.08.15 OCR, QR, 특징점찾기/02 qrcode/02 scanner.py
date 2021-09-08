import cv2
from pyzbar import pyzbar

img = cv2.imread('img/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

qrcodes = pyzbar.decode(gray)
print(f'{len(qrcodes)} 개 인식')

if qrcodes:
    for qrcode in qrcodes:
        print(f'{qrcode.type}, {qrcode.data.decode("utf-8")}')