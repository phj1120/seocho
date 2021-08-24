import cv2
import numpy as np
import tensorflow as tf

label = ['red', 'green', 'blue', 'yellow', 'none']
interpreter = tf.lite.Interpreter(model_path='model/model_unquant.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

cap = cv2.VideoCapture(0)
cap.set(3, 224)
cap.set(4, 224)

while True:
    ret, frame = cap.read()

    if ret:
        frame = cv2.resize(frame, dsize=(224, 224))
        dst = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('video', frame)

        input_data = np.array([dst], dtype=np.float32)
        input_data = input_data / 255.0
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])

        print(label[np.argmax(output_data[0])], *output_data)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()