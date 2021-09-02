# 교수님이 도와주신 파일

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

# load the serialized face detector model from disk
my_path = './'
prototxtPath = os.path.join(my_path, 'face_detector/deploy.prototxt')
weightsPath = os.path.join(my_path, 'face_detector/res10_300x300_ssd_iter_140000.caffemodel')
net = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
model_path = os.path.join(my_path, 'mask_detector.model')
model = load_model(model_path)

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height

while True:
    ret, img = cap.read()
    orig = img.copy()
    (h, w) = img.shape[:2]

    # construct a blob from the image
    blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the face detection
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence associated with the detection
        confidence = detections[0, 0, i, 2]

        # 가장 큰 박스만 가져오게 for문으로
        # filter out weak detections by ensuring the confidence is greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x,y)-coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            #
            if box[0] * box[1] * box[2] * box[3]:
                distance = box[2] - box[0]
                print(distance)
                if distance > 200:
                    # ensure the bounding boxes fall within the dimensions of the frame
                    (startX, startY) = (max(0, startX), max(0, startY))
                    (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

                    # extract the face ROI, convert if from BGR to RGB channel ordering, resize it to 224x224, and preprocess it
                    face = img[startY:endY, startX:endX]

                    # 사진이 커지면 얼굴 위치 값이 잘못 되는 경우가 있어 이를 해결하기 위해 np로 바꿔 있을때만
                    # 코드 실행되도록 처리
                    arr = np.array([])
                    flag = not np.any(face)

                    if not flag:
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                        face = cv2.resize(face, (244, 244))
                        face = img_to_array(face)
                        face = preprocess_input(face)
                        face = np.expand_dims(face, axis=0)

                        # pass the face through the model to determine if the face has a mask or not
                        (mask, withoutMask) = model.predict(face)[0]

                        # determine the class label and color we'll use to draw the bounding box and text
                        label = "Mask" if mask > withoutMask else "No Mask"
                        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

                        # include the confidence level to the label
                        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

                        # display the label and bounding box rectangle on the output frame
                        cv2.putText(img, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                        cv2.rectangle(img, (startX, startY), (endX, endY), color, 2)

    cv2.imshow("Output", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
