import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from eunjeon import Mecab

# 전처리 데이터 불러오기
train_data = pd.read_csv("../99.data/NaverMovieReview/train_data.csv")
test_data = pd.read_csv("../99.data/NaverMovieReview/test_data.csv")


# 토큰화
mecab = Mecab()

## 불용어
stopwords = ["도", "는", "다", "의", "가", "이", "은", "한", "에", "하", "고", "을", "를", "인", "듯", "과", "와", "네", "들", "듯", "지", "임", "게"]

## 훈련 데이터
train_data["토큰화"] = train_data["리뷰"].apply(mecab.morphs)
train_data["토큰화"] = train_data["토큰화"].apply(lambda x: [item for item in x if item not in stopwords])
# 검증 데이터
test_data["토큰화"] = test_data["리뷰"].apply(mecab.morphs)
test_data["토큰화"] = test_data["토큰화"].apply(lambda x: [item for item in x if item not in stopwords])


# 긍정 리뷰의 평균 길이
## matplotlib 한글 출력
## C:/Windows/Fonts/ 에 있는 폰트 아무거나 위치 지정
fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/batang.ttc'
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

pos_len = train_data[train_data["분류"]==1]["토큰화"].map(lambda x: len(x))
print("긍정 리뷰의 평균 길이 :", np.mean(pos_len))
neg_len = train_data[train_data["분류"]==0]["토큰화"].map(lambda x: len(x))
print("부정 리뷰의 평균 길이 :", np.mean(neg_len))

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,5))
ax1.hist(pos_len, color="red")
ax1.set_title("긍정 리뷰")
ax1.set_xlabel("긍정 리뷰 길이")
ax1.set_ylabel("긍정 리뷰 갯수")

ax2.hist(neg_len, color="blue")
ax2.set_title("부정 리뷰")
ax2.set_xlabel("부정 리뷰 길이")
ax2.set_ylabel("부정 리뷰 갯수")
plt.show()


# 데이터셋
x_train_tokenized = train_data["토큰화"].values
y_train_tokenized = train_data["분류"].values
x_test_tokenized = test_data["토큰화"].values
y_test_tokenized = test_data["분류"].values


# 데이터셋 저장
# allow_pickle 생략해도 되는데 기본이 True임(객체 배열 저장을 허용)
np.save("../99.data/NaverMovieReview/x_train_tokenized.npy", x_train_tokenized)
np.save("../99.data/NaverMovieReview/y_train_tokenized.npy", y_train_tokenized)
np.save("../99.data/NaverMovieReview/x_test_tokenized.npy", x_test_tokenized)
np.save("../99.data/NaverMovieReview/y_test_tokenized.npy", y_test_tokenized)