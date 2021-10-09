import numpy as np
from tensorflow.keras.layers import Embedding, Dense, GRU
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


# 데이터 불러오기
x_train = np.load("../99.data//NaverShoppingReview/x_train_padded.npy")
y_train = np.load("../99.data//NaverShoppingReview/y_train_tokenized.npy")
x_test = np.load("../99.data//NaverShoppingReview/x_test_padded.npy")
y_test = np.load("../99.data//NaverShoppingReview/y_test_tokenized.npy")


# 모델 생성
## 정수 인코딩을 통해서 구한 사이즈
vocab_size = 21022

model = Sequential()
model.add(Embedding(vocab_size, 100))
model.add(GRU(128))
model.add(Dense(1, activation="sigmoid"))

# 모델 컴파일
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])


# 모델 훈련
## EarlyStopping, 과적합으로 손실이 4회이상 발생하면 조기 종료
es = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=4)

## ModelCheckpoint, 검증 데이터의 정확도가 이전보다 좋아질때만 모델을 저장
mc = ModelCheckpoint("../98.models/NaverShoppingReview/best_model_GRU.h5", monitor="val_acc", mode="max", verbose=1, save_best_only=True)

history = model.fit(
    x_train, y_train,
    epochs=20,
    batch_size=100,
    callbacks=[es, mc],
    validation_data=(x_test, y_test),
    verbose=1
)


# 모델 평가
loss, acc = model.evaluate(x_test, y_test)
print('정확도: {:5.2f}%'.format(100 * acc))