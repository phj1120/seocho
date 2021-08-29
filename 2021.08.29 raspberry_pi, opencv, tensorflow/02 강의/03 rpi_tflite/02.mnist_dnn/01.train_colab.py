import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models


(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

train_images = train_images.reshape((-1, 28*28))
test_images = test_images.reshape((-1, 28*28))

train_images = train_images / 255.0
test_imates = test_images / 255.0

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=((28*28, ))))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=100)

# saved_model 형식으로 모델 저장
tf.saved_model.save(model, "/content/model")

# tflite 모델로 변환
converter = tf.lite.TFLiteConverter.from_saved_model('/content') # path to the SavedModel directory
tflite_model = converter.convert()

# 변환된 모델 저장
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)
