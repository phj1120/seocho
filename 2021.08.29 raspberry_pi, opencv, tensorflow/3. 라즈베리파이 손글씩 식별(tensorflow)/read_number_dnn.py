import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from gpiozero import LED

interpreter = tflite.Interpreter(model_path='model/dnn_model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)


cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 320)

while True:
    ret, frame = cap.read()

    if ret:
        img = cv2.resize(frame, dsize=(28, 28))
        cv2.imshow('video', frame)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img = np.array(gray_img, dtype=np.float32)
        gray_img = 255 - gray_img
        
        input_data = gray_img.reshape(1, 28*28, )
        input_data = input_data/255.0
        
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        
        output_data = interpreter.get_tensor(output_details[0]['index'])

        result = np.argmax(output_data[0])
        print(result)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()