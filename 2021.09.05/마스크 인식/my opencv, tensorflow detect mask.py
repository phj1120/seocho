from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

my_path = './'
# 얼굴 인식 모델 로드
prototxtPath = os.path.join(my_path, 'face_detector/deploy.prototxt')
weightsPath = os.path.join(my_path, 'face_detector/res10_300x300_ssd_iter_140000.caffemodel')
net = cv2.dnn.readNet(prototxtPath, weightsPath)

# 마스크 착용 여부 판단 모델 로드
model_path = os.path.join(my_path, 'mask_detector.model')
model = load_model(model_path)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    orig = img.copy()
    (h, w) = img.shape[:2]

    # blob 이미지 생성
    blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))
    # 얼굴 인식
    net.setInput(blob)
    detections = net.forward()

    # 가장 크게 인식된 박스 하나만 가져오도록
    largest_index = 0
    largest_distance = 0
    # 라즈베리파이 이용시 처리량 줄이기 위해 줄임
    # for i in range(0, detections.shape[2]):
    for i in range(0, 10):
        # 얼굴 인식 확률
        confidence = detections[0, 0, i, 2]
        # 인식된 확률이 최소 확률보다 큰 경우
        if confidence > 0.5:
            # boundig box 좌표 계산
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])

            distance = box[2] - box[0]
            if distance >= largest_distance:
                largest_distance = distance
                largest_index = i
                largest_box = box

    # 가장 큰 박스의 크기가 일정 크기 이상일 경우
    if largest_distance > 200:
        # bounding box 가 이미지를 벗어나면 가장 끝단을 값으로
        (startX, startY, endX, endY) = box.astype("int")
        (startX, startY) = (max(0, startX), max(0, startY))
        (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
        # 박스에서 얼굴 잘라 배열에 저장
        face = img[startY:endY, startX:endX]

        # 얼굴 추출이 됐을 경우 ( 가까이 간 경우 오류 발생 )
        if np.any(face):
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (244, 244))
            face = img_to_array(face)
            face = preprocess_input(face)
            face = np.expand_dims(face, axis=0)

            # mask와 withoutMask 에 각각의 확률 예측
            (mask, withoutMask) = model.predict(face)[0]

            # 화면에 표시할 라벨 저장 및 색상 지정
            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

            # 라벨에 확률 추가
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

            # 이미지에 라벨 추가
            cv2.putText(img, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            # 이미지에 사각형 추가
            cv2.rectangle(img, (startX, startY), (endX, endY), color, 2)

    cv2.imshow("Output", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()