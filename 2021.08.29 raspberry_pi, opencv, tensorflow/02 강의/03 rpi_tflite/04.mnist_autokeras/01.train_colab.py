import numpy as np
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.datasets import mnist

import autokeras as ak

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 훈련
clf = ak.ImageClassifier(overwrite=True, max_trials=1)
# 이미지를 이용해 훈련
clf.fit(x_train, y_train)

# 최적의 모델로 예측
predicted_y = clf.predict(x_test)
print(predicted_y)

# 테스트 데이터로 최적의 모델 평가
print(clf.evaluate(x_test, y_test))

# 저장된 모델 변환
converter = tf.lite.TFLiteConverter.from_saved_model('/content') # path to the SavedModel directory
tflite_model = converter.convert()

# 변환된 모델 저장
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)
