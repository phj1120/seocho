import cv2, os, time
import numpy as np
from gpiozero import LED

# LED 설정
red_led = LED(14)
green_led = LED(15)
blue_led = LED(18)
yellow_led = LED(17)

# 카메라 설정
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)


while True:
    ret, frame = cap.read()
    # 영상 촬영 중 이라면
    if ret:
        # HSV 형식에 맞게 변환
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 해당 범위의 색상만 인식
        mask_red = cv2.inRange(frame_HSV, (170, 100, 100), (180, 255, 255))
        mask_green = cv2.inRange(frame_HSV, (50, 100, 100), (70, 255, 255))
        mask_blue = cv2.inRange(frame_HSV, (110, 100, 100), (130, 255, 255))
        mask_yellow = cv2.inRange(frame_HSV, (10, 100, 100), (40, 255, 255))

        # 빨간색 인식
        red = np.array(mask_red).reshape((240 * 320,))
        red_count = np.count_nonzero(red)
        # 해당 색상의 픽셀이 특정 숫자 이상이 된다면 콘솔에 결과 출력, LED on
        if red_count >= 3000:
            print('red')
            red_led.on()
        else:
            red_led.off()

        # 노란색 인식
        yellow = np.array(mask_yellow).reshape((240 * 320,))
        yellow_count = np.count_nonzero(yellow)
        if yellow_count >= 3000:
            print('yellow')
            yellow_led.on()
        else:
            yellow_led.off()

        # 초록색 인식
        green = np.array(mask_green).reshape((240 * 320,))
        green_count = np.count_nonzero(green)
        if green_count >= 3000:
            print('green')
            green_led.on()
        else:
            green_led.off()

        # 파란색 인식
        blue = np.array(mask_blue).reshape((240 * 320,))
        blue_count = np.count_nonzero(blue)
        if blue_count >= 3000:
            print('blue')
            blue_led.on()
        else:
            blue_led.off()

        # 결과를 이미지로 볼 수 있도록 합침
        total = red + green + yellow + blue
        mask_total = np.reshape(total, (240, 320,))

        # 색상이 인식된 부분만 표시
        result_img = cv2.bitwise_and(frame, frame, mask=mask_total)

        # 결과값 한번에 확인시 사용
        # print(red_count, green_count, blue_count, yellow_count)

        cv2.imshow('ori', frame)
        cv2.imshow('result', result_img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()