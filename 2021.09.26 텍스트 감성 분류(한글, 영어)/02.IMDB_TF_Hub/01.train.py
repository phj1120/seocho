import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_hub as hub
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# 데이터셋 다운로드
train_data, test_data = tfds.load(name="imdb_reviews", split=["train", "test"], batch_size=-1, as_supervised=True)
x_train, y_train = tfds.as_numpy(train_data)
x_test, y_test = tfds.as_numpy(test_data)
print('훈련 데이터 : {:,}개'.format(len(x_train)))
print('검증 데이터 : {:,}개'.format(len(x_test)))

# 구조 확인
print(x_train[:10])
print(y_train[:10])

# 검증 데이터셋 준비하기
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

# 검증 데이터셋 준비하기
hub_model = "https://tfhub.dev/google/nnlm-en-dim50/2"
hub_layer = hub.KerasLayer(hub_model, input_shape=[], dtype=tf.string, trainable=True)

# 모델 생성
model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(1))
model.summary()

# 모델 컴파일
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])

# 모델 훈련
# EarlyStopping, 과적합으로 손실이 4회이상 발생하면 조기 종료
es = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=4)

# ModelCheckpoint, 검증 데이터의 정확도가 이전보다 좋아질때만 모델을 저장
mc = ModelCheckpoint("../98.models/imdb/best_model_nnlm-en-dim50_v2.h5", monitor="val_acc", mode="max", verbose=1, save_best_only=True)

history = model.fit(
    x_train, y_train,
    epochs=40,
    batch_size=512,
    callbacks=[es, mc],
    validation_data=(x_test, y_test),
    verbose=1
)

# 모델 평가
loss, acc = model.evaluate(x_test, y_test)
print('정확도: {:5.2f}%'.format(100 * acc))