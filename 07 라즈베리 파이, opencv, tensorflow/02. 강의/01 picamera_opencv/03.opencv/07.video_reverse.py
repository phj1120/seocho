import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height

while True:
    ret, img = cap.read()
    rl_flip_img = cv2.flip(img, 1)  # right/left
    tb_flip_img = cv2.flip(img, 0)  # top/bottom

    cv2.imshow('rl_flip_camera', rl_flip_img)
    cv2.imshow('tb_flip_camera', tb_flip_img)

    # press 'ESC' to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
