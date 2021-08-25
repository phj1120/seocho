import cv2, os, time
import numpy as np
from gpiozero import LED

red_led = LED(14)
green_led = LED(15)
blue_led = LED(18)
yellow_led = LED(17)

cap=cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('no camera') 
    else:
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_red = cv2.inRange(frame_HSV, (170, 100, 100), (180, 255, 255))
        mask_green = cv2.inRange(frame_HSV, (50, 100, 100), (70, 255, 255))
        mask_blue = cv2.inRange(frame_HSV, (110, 100, 100), (130,255,255))
        mask_yellow = cv2.inRange(frame_HSV, (10,100,100), (40,255,255))
        
        red = np.array(mask_red).reshape((240*320, ))
        red_count = np.count_nonzero(red)
        if red_count >= 3000:
            print('red')
            red_led.on()
        else:
            red_led.off()
        
        yellow = np.array(mask_yellow).reshape((240*320, ))
        yellow_count = np.count_nonzero(yellow)
        if yellow_count >= 3000:
            print('yellow')
            yellow_led.on()
        else:
            yellow_led.off()
            
        green = np.array(mask_green).reshape((240*320, ))
        green_count = np.count_nonzero(green)
        if green_count >= 3000:
            print('green')
            green_led.on()
        else:
            green_led.off()
            
        blue = np.array(mask_blue).reshape((240*320, ))
        blue_count = np.count_nonzero(blue)
        if blue_count >= 3000:
            print('blue')
            blue_led.on()
        else:
            blue_led.off()
            
        total = red + green + yellow + blue
        mask_total = np.reshape(total, (240, 320, ))
        result_img = cv2.bitwise_and(frame, frame, mask = mask_total)
        
        print(red_count, green_count, blue_count, yellow_count)
        
        cv2.imshow('ori', frame)
        cv2.imshow('result', result_img)
    
    if cv2.waitKey(1) & 0xFF == 27:
       break
    
cap.release()
cv2.destroyAllWindows()