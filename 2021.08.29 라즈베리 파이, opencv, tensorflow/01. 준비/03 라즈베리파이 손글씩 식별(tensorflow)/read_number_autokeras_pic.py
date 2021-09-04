import cv2, os
import numpy as np
import tflite_runtime.interpreter as tflite
from gpiozero import LED

interpreter = tflite.Interpreter(model_path='model/autokeras_model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print('autokeras')


file_path = '/home/pi/Desktop/seocho/2021.08.29 raspberry_pi, opencv, tensorflow/3. 라즈베리파이 손글씩 식별(tensorflow)/mnist  숫자'
files = os.listdir(file_path)
for file in files:
    frame = cv2.imread(f'{file_path}/{file}')
    img = cv2.resize(frame, dsize=(28, 28))
    cv2.imshow('video', frame)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = np.array(gray_img, dtype=np.uint8)
    gray_img = 255 - gray_img
    input_data = gray_img.reshape(1, 28, 28, )
    #print(input_data.shape)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])

    result = np.argmax(output_data[0])
    print(file, ' -> ',result)
cv2.destroyAllWindows()