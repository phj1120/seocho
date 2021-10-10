import board, adafruit_mlx90614
from gpiozero import LED, Buzzer
from rpi_lcd import LCD
from time import sleep

import tflite_runtime.interpreter as tflite
import numpy as np
import cv2
import os

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# GPIO 제어 함수 생성
def my_status(buzzer_state=False, red_led_state=False, green_led_state=False, blue_led_state=False, lcd_text=['','']):
    buzzer.on() if buzzer_state else buzzer.off()
    red_led.on() if red_led_state else red_led.off()
    green_led.on() if green_led_state else green_led.off()
    blue_led.on() if blue_led_state else blue_led.off()
    lcd.text(f'{lcd_text[0]:^16s}', 1)
    lcd.text(f'{lcd_text[1]:^16s}', 2)

# GPIO 관련 설정
i2c = board.I2C()
mlx = adafruit_mlx90614.MLX90614(i2c)
lcd = LCD()

buzzer = Buzzer(23)
red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

print('START')

#  OpenCV를 이용한 얼굴 위치 감지
cascPath = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# 마스크 착용 여부 확인을 위한 모델 로드
interpreter = tflite.Interpreter(model_path='../99 model/mask_detector_224.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 카메라 설정
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    # 가장 큰 얼굴 값을 찾는데 사용할 변수 선언
    largest_face_area = 0
    largest_face_box = (0, 0, 0, 0)
    # 얼굴 값이 있는 경우
    if np.any(faces):
        # faces 에서 좌표 가져옴
        for (x, y, w, h) in faces:
            # 좌표 이용해서 얼굴 자름
            face_frame = frame[y:y + h, x:x + w]
            # 가장 큰 얼굴 찾기
            area = w*h
            if largest_face_area < area:
                largest_face_area = area
                largest_face_frame = face_frame
                largest_face_box = faces
        print(largest_face_area)
        # 가장 큰 얼굴의 값이 일정 값 이상인 경우
        if largest_face_area > 40000:
            # 마스크 착용 여부 예측을 위한 이미지 처리
            (x, y, w, h) = largest_face_box[0]
            face_frame = cv2.resize(largest_face_frame, (224, 224))
            face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
            face_frame = img_to_array(face_frame)
            face_frame = np.expand_dims(face_frame, axis=0)
            face_frame = preprocess_input(face_frame)

            # tflite 이용해 예측
            interpreter.set_tensor(input_details[0]['index'], face_frame)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])

            # 결과 값 사용
            (mask, withoutMask) = output_data[0]
            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
            
            # 사진에 label 추가
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            # 사진에 박스 추가
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            
            # 온도 체크 시작
            temp = mlx.object_temperature
            # 마스크를 안 쓴 경우 : 착용 경고
            if mask < withoutMask:
                my_status(buzzer_state=True, red_led_state=True, lcd_text=['No Pass', f'No Mask'])
            # 일정 온도 이상인 경우 : 온도 경고
            elif temp >= 35.0:
                my_status(buzzer_state=True, red_led_state=True, lcd_text=['No Pass', f'Temp : {temp:.1f}'])
            # 일정 온도 이하인 경우 : 통과
            else:
                my_status(green_led_state=True, lcd_text=['Pass', f'Temp : {temp:.1f}'])
        # 가장 큰 얼굴 값이 일정 값 이하인 경우
        else:
            my_status(blue_led_state=True, lcd_text=['Wait', 'Come Closer '])
    # 얼굴이 탐지되지 않았을 경우
    else:
        my_status(blue_led_state=True, lcd_text=['Wait', 'No Face'])
    # 화면 출력
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()