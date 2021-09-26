from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 단어제한(10,000개)을 두고 데이터셋 새로 불러오기
vocab_size = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

# 패딩 처리
# 리뷰 최대 길이를 500으로 제한
max_len = 500
x_train = pad_sequences(x_train, maxlen=max_len)
x_test = pad_sequences(x_test, maxlen=max_len)

# 모델 생성
# 텍스트에는 LSTM, GRU 많이 사용하는데 교수님은 LSTM 선호
# 1과 0으로 명확하게 구분지어야 하는 상황이라면 sigmoid 쓰는 것이 좋음
model = Sequential()
model.add(Embedding(vocab_size, 100))
model.add(LSTM(128))
model.add(Dense(1, activation="sigmoid"))
model.summary()

# 모델 컴파일
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["acc"]
)

# 모델 훈련
history = model.fit(
    x_train, y_train,
    epochs=20,
    batch_size=512,
    validation_data=(x_test, y_test),
    verbose=1
)

# 모델 평가
loss, acc = model.evaluate(x_test, y_test)
print('정확도: {:5.2f}%'.format(100 * acc))

# 시간 경과에 따른 정확도
history_dict = history.history
acc = history_dict['acc']
val_acc = history_dict['val_acc']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.clf()   # clear figure

# 시간 경과에 따른 손실 그래프 생성
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()