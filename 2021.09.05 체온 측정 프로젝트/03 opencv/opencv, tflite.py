import cv2
import os
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# import tflite_runtime.interpreter as tflite
import tensorflow as tf
import numpy as np


cascPath = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

interpreter = tf.lite.Interpreter(model_path='mask_detector_224.tflite')
# interpreter = tflite.Interpreter(model_path='mask_detector_224.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)
#
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    faces_list = []
    preds = []

    largest_face_area = 0
    largest_face_box = (0, 0, 0, 0)
    if np.any(faces):
        for (x, y, w, h) in faces:
            face_frame = frame[y:y + h, x:x + w]
            face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
            face_frame = cv2.resize(face_frame, (224, 224))
            face_frame = img_to_array(face_frame)
            face_frame = np.expand_dims(face_frame, axis=0)
            face_frame = preprocess_input(face_frame)
            area = w*h
            if largest_face_area < area:
                largest_face_area = area
                largest_face_frame = face_frame
                largest_face_box = faces
                # print(face_frame, face_frame.shape)

        if largest_face_area > 40000:
            (x, y, w, h) = largest_face_box[0]
            interpreter.set_tensor(input_details[0]['index'], largest_face_frame)
            interpreter.invoke()

            output_data = interpreter.get_tensor(output_details[0]['index'])
            # print(output_data[0])
            (mask, withoutMask) = output_data[0]

            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            print(largest_face_area)
        # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()