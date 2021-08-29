"""
https://www.tensorflow.org/lite/guide/python?hl=ko
https://gpiozero.readthedocs.io/en/stable/api_output.html#rgbled
pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
"""

import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from gpiozero import RGBLED


led = RGBLED(14, 15, 18)

# label
label = ['red', 'green', 'blue', 'yellow', 'none']

# model
interpreter = tflite.Interpreter(model_path='model_unquant.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, dsize=(224, 224))
    dst = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    input_data = np.array([dst], dtype=np.float32)
    input_data = input_data / 255.0
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    result = label[np.argmax(output_data[0])]
    print(result, *output_data)

    if result == 'red':
        led.color = (1, 0, 0)
    elif result == 'green':
        led.color = (0, 1, 0)
    elif result == 'blue':
        led.color = (0, 0, 1)
    else:
        led.color = (0, 0, 0)

    cv2.imshow('img', img)

    # press 'ESC' to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
