import pandas as pd
import numpy as np
from eunjeon import Mecab

# 전처리 데이터 불러오기
train_data = pd.read_csv("../99.data/NaverShoppingReview/train_data.csv")
test_data = pd.read_csv("../99.data/NaverShoppingReview/test_data.csv")

# 토큰화
mecab = Mecab()

stopwords = ["도", "는", "다", "의", "가", "이", "은", "한", "에", "하", "고", "을", "를", "인", "듯", "과", "와", "네", "들", "듯", "지", "임", "게"]

# apply 일괄 적용
# lambda 익명 함수(간단한 함수)
# lambda x: [item for item in x if item not in stopwords]
# 토큰화에 있는 데이터를 item 이라는 이름으로 불러오고 stopwords에 없으면 불러오고 없으면 버려라?
train_data["토큰화"] = train_data["리뷰"].apply(mecab.morphs)
train_data["토큰화"] = train_data["토큰화"].apply(lambda x: [item for item in x if item not in stopwords])

test_data["토큰화"] = test_data["리뷰"].apply(mecab.morphs)
test_data["토큰화"] = test_data["토큰화"].apply(lambda x: [item for item in x if item not in stopwords])

# 확인
pos_len = train_data[train_data["분류"]==1]["토큰화"].map(lambda x: len(x))
print("긍정 리뷰의 평균 길이 :", np.mean(pos_len))
neg_len = train_data[train_data["분류"]==0]["토큰화"].map(lambda x: len(x))
print("부정 리뷰의 평균 길이 :", np.mean(neg_len))

# 데이터셋
x_train_tokenized = train_data["토큰화"].values
y_train_tokenized = train_data["분류"].values
x_test_tokenized = test_data["토큰화"].values
y_test_tokenized = test_data["분류"].values

# 저장
np.save("../99.data/NaverShoppingReview/x_train_tokenized.npy", x_train_tokenized, allow_pickle=True)
np.save("../99.data/NaverShoppingReview/y_train_tokenized.npy", y_train_tokenized)
np.save("../99.data/NaverShoppingReview/x_test_tokenized.npy", x_test_tokenized, allow_pickle=True)
np.save("../99.data/NaverShoppingReview/y_test_tokenized.npy", y_test_tokenized)