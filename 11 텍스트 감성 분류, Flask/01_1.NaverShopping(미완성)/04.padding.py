import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences

# 데이터 로드
x_train_encoded = np.load("../99.data/NaverShoppingReview/x_train_encoded.npy", allow_pickle=True)
x_test_encoded = np.load("../99.data/NaverShoppingReview/x_test_encoded.npy", allow_pickle=True)

# 리뷰 최대 길이, 평균 길이
print("리뷰의 최대 길이 : {:,}".format(max(len(l) for l in x_train_encoded)))
print("리뷰의 평균 길이 : {:,.2f}".format(sum(map(len, x_train_encoded))/len(x_train_encoded)))


# 리뷰 최대 길이 선정
max_len = 80
cnt = 0
for s in x_train_encoded:
    if len(s) <= max_len:
        cnt = cnt + 1
print("리뷰 길이가 {} 이하인 비율: {:.8f}%".format(max_len, (cnt / len(x_train_encoded))*100))

# 패딩 처리
x_train_padded = pad_sequences(x_train_encoded, maxlen = max_len)
x_test_padded = pad_sequences(x_test_encoded, maxlen = max_len)

# 저장
np.save("../99.data/NaverShoppingReview/x_train_padded.npy", x_train_padded, allow_pickle=True)
np.save("../99.data/NaverShoppingReview/x_test_padded.npy", x_test_padded, allow_pickle=True)