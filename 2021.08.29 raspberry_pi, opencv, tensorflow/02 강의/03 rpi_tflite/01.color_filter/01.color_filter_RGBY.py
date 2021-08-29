"""
https://www.tensorflow.org/lite/guide/python?hl=ko
pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
"""

import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from gpiozero import LED


red_led = LED(14)
green_led = LED(15)
blue_led = LED(18)
yellow_led = LED(17)

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
        red_led.on()
        blue_led.off()
        green_led.off()
        yellow_led.off()
    elif result == 'green':
        red_led.off()
        blue_led.off()
        green_led.on()
        yellow_led.off()
    elif result == 'blue':
        red_led.off()
        blue_led.on()
        green_led.off()
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

    cv2.imshow('img', img)

    # press 'ESC' to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
