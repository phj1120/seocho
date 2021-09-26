import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터셋 불러오기
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt", filename="../99.data/NaverMovieReview/ratings_train.txt")
train_data = pd.read_table("../99.data/NaverMovieReview/ratings_train.txt")
train_data = train_data.rename(columns={"document": "리뷰", "label": "분류"})
print("리뷰 갯수 : {:,}개".format(len(train_data)))
train_data[:5]

# 검증용
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", filename="../99.data/NaverMovieReview/ratings_test.txt")
test_data = pd.read_table("../99.data/NaverMovieReview/ratings_test.txt")
test_data = test_data.rename(columns={"document": "리뷰", "label": "분류"})
print("리뷰 갯수 : {:,}개".format(len(test_data)))
test_data[:5]

# 중복된 리뷰 제거, 빈 값 제거
train_data.drop_duplicates(subset=["리뷰"],  inplace=True)
train_data = train_data.dropna(how="any")
print(len(train_data))

test_data.drop_duplicates(subset=["리뷰"],  inplace=True)
test_data = test_data.dropna(how="any")
print(len(test_data))

# 코랩에서는 되는데 pc에서는 안됨
# 확인, 전처리

# 훈련 데이터 분류(긍정, 부정) 확인
train_data["분류"].value_counts().plot(kind = "bar")
print(train_data.groupby("분류").size().reset_index(name = "갯수"))

# 전처리
# PC의 경우 regex=True 추가(버전 맞추기 위해)
train_data["리뷰"] = train_data["리뷰"].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","", regex=True)
train_data["리뷰"].replace("", np.nan, inplace=True)
train_data = train_data.dropna(how="any")

# 위치 지정
train_data.to_csv("../99.data/NaverMovieReview/train_data.csv")
test_data.to_csv("../99.data/NaverMovieReview/test_data.csv")