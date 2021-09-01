import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from gpiozero import LED

# LED 설정
red_led = LED(14)
green_led = LED(15)
blue_led = LED(18)
yellow_led = LED(17)

# 라벨 생성
label = ['red', 'green', 'blue', 'yellow', 'none']

# 모델 로드
interpreter = tflite.Interpreter(model_path='model/model_unquant.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
# print(input_details)

# 카메라 캡쳐 시작
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # input_details 조건에 맞게 형식 변경
        frame = cv2.resize(frame, dsize=(224, 224))
        dst = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('video', frame)

        input_data = np.array([dst], dtype=np.float32)
        input_data = input_data / 255.0
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])

        result = label[np.argmax(output_data[0])]
        # print(result, *output_data)

        if result == 'red':
            red_led.on()
            blue_led.off()
            green_led.off()
            yellow_led.off()
        elif result == 'blue':
            red_led.off()
            blue_led.on()
            green_led.off()
            yellow_led.off()
        elif result == 'green':
            red_led.off()
            blue_led.off()
            green_led.on()
            yellow_led.off()
        elif result == 'yellow':
            red_led.off()
            blue_led.off()
            green_led.off()
            yellow_led.on()
        else:
            red_led.off()
            blue_led.off()
            green_led.off()
            yellow_led.off()

        print(result)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()