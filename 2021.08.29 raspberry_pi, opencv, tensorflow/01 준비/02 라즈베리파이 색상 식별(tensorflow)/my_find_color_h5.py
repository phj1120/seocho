from tensorflow.keras.models import load_model
# from PIL import Image, ImageOps
import numpy as np
import cv2
# Load the model
model = load_model('converted_keras/keras_model.h5')
label = ['red', 'green', 'blue', 'yellow', 'none']

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

cap = cv2.VideoCapture(0)
cap.set(3, 224)
cap.set(4, 224)

while True:
    ret, frame = cap.read()

    if ret:
        frame = cv2.resize(frame, dsize=(224, 224))
        dst = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('video', frame)

        # turn the image into a numpy array
        image_array = np.asarray(dst)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)
        print(label[np.argmax(prediction[0])])

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

