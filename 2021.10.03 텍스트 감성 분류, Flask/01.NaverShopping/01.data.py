import urllib.request

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

# 네이버 쇼핑 리뷰 다운로드
urllib.request.urlretrieve("https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt",
                           filename="naver_shopping.txt")

# 가공이 용이하도록 names 붙여줌
data = pd.read_table("naver_shopping.txt", names=["평점", "리뷰"])
print("리뷰 갯수 : {:,}개".format(len(data)))

# 리뷰 출력
print(data.head(10)) # pandas
print(data[:10]) # 배열
'''
## 데이터 셋을 보면 1~5점 으로 별점을 나눔
5, 4 - 긍정
3    - 제외
2, 1 - 부정
분류를 직접 추가
1 - 긍정
0 - 부정
'''
data["분류"] = np.select([data["평점"]>3], [1], default=0)
print(data[:10])

# 중복 리뷰 제거
data.drop_duplicates(subset=["리뷰"], inplace=True)
print("리뷰 갯수 : {:,}개".format(len(data)))

# 빈 값 제거
data = data.dropna(how='any')
print("리뷰 갯수 : {:,}개".format(len(data)))

# 학습 데이터와 검증 데이터를 7:3 비율로 나눔
# sklearn 라이브러리 이용
train_data, test_data = train_test_split(data, test_size = 0.3, shuffle=True, random_state = 42)
print("학습 데이터 갯수 : {:,}개".format(len(train_data)))
print("검증 데이터 갯수 : {:,}개".format(len(test_data)))

# 훈련 데이터 긍정 부정 확인
train_data["분류"].value_counts().plot(kind = "bar")
print(train_data.groupby("분류").size().reset_index(name = "갯수"))

# 전처리
train_data["리뷰"] = train_data["리뷰"].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
train_data["리뷰"].replace("", np.nan, inplace=True)
# train_data = train_data.dropna(how='any')

test_data["리뷰"] = test_data["리뷰"].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
test_data["리뷰"].replace("", np.nan, inplace=True)
# test_data = test_data.dropna(how='any')

train_data.to_csv("../99.data/NaverShoppingReview/train_data.csv")
test_data.to_csv("../99.data/NaverShoppingReview/test_data.csv")
