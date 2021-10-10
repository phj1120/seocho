import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

# 데이터 로드
x_train_tokenized= np.load("../99.data/NaverShoppingReview/x_train_tokenized.npy", allow_pickle=True)
x_test_tokenized= np.load("../99.data/NaverShoppingReview/x_test_tokenized.npy", allow_pickle=True)

# 단어 집합 분석
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_train_tokenized)

threshold = 2
total_cnt = len(tokenizer.word_index) # 단어의 수
rare_cnt = 0 # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
total_freq = 0 # 훈련 데이터의 전체 단어 빈도수 총 합
rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

# 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
for key, value in tokenizer.word_counts.items():
    total_freq = total_freq + value

    # 단어의 등장 빈도수가 threshold보다 작으면
    if value < threshold:
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value

print("단어 집합(vocabulary)의 크기 : {:,}".format(total_cnt))
print("등장 빈도가 {}번 이하인 희귀 단어의 수 :  {:,}개".format(threshold - 1, rare_cnt))
print("단어 집합에서 희귀 단어의 비율 :  {:.2f}%".format(rare_cnt / total_cnt * 100))
print("전체 등장 빈도에서 희귀 단어 등장 빈도 비율 :  {:.2f}%".format(rare_freq / total_freq * 100))

# 단어 크기 제한
vocab_size = total_cnt - rare_cnt + 2
print("단어 집합의 크기 : {:,}".format(vocab_size))

# 정수 인코딩
tokenizer = Tokenizer(vocab_size, oov_token = "OOV")
tokenizer.fit_on_texts(x_train_tokenized)
x_train_encoded = tokenizer.texts_to_sequences(x_train_tokenized)
x_test_encoded = tokenizer.texts_to_sequences(x_test_tokenized)

# 정수 인코딩 데이터 저장
x_train_encoded = np.array(x_train_encoded, dtype="object")
x_test_encoded = np.array(x_test_encoded, dtype="object")
np.save("../99.data/NaverShoppingReview/x_train_encoded.npy", x_train_encoded, allow_pickle=True)
np.save("../99.data/NaverShoppingReview/x_test_encoded.npy", x_test_encoded, allow_pickle=True)