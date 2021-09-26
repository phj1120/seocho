import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# 데이터셋 다운로드
# 단어제한(10,000개)을 두고 데이터셋 불러오기
vocab_size = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)
print('훈련 데이터 : {:,}개'.format(len(x_train)))
print('검증 데이터 : {:,}개'.format(len(x_test)))

# 패딩
max_len = 500
x_train = pad_sequences(x_train, maxlen=max_len)
x_test = pad_sequences(x_test, maxlen=max_len)

# 모델 생성
model = Sequential()
model.add(Embedding(vocab_size, 100))
model.add(LSTM(128))
model.add(Dense(1, activation="sigmoid"))
model.summary()

# 모델 컴파일
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])

# 모델 훈련
# EarlyStopping, 과적합으로 손실이 4회이상 발생하면 조기 종료
es = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=4)

# ModelCheckpoint, 검증 데이터의 정확도가 이전보다 좋아질때만 모델을 저장
mc = ModelCheckpoint("../models/imdb/best_model_LSTM.h5", monitor="val_acc", mode="max", verbose=1, save_best_only=True)

history = model.fit(
    x_train, y_train,
    epochs=20,
    batch_size=512,
    callbacks=[es, mc],
    validation_data=(x_test, y_test),
    verbose=1
)

# 모델 평가
loss, acc = model.evaluate(x_test, y_test)
print('정확도: {:5.2f}%'.format(100 * acc))