import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from rpi_lcd import LCD


lcd = LCD()

interpreter = tflite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 320)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, dsize=(28, 28))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.array(gray, dtype=np.float32)
    gray = 255 - gray

    input_data = gray.reshape(1, 28 * 28, )
    input_data = input_data / 255.0

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])

    result = np.argmax(output_data[0])
    lcd.text("NUMBER", 1)
    lcd.text(str(result), 2)
    print(result)

    cv2.imshow('img', img)

    # press 'ESC' to quit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()