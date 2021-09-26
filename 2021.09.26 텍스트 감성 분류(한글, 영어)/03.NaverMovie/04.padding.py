import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.font_manager as fm

# 정수 인코딩 데이터 불러오기
x_train_encoded = np.load("../99.data/NaverMovieReview/x_train_encoded.npy", allow_pickle=True)
x_test_encoded = np.load("../99.data/NaverMovieReview/x_test_encoded.npy", allow_pickle=True)


# 리뷰 최대 길이, 평균 길이
## matplotlib 한글 출력
## C:/Windows/Fonts/ 에 있는 폰트 아무거나 위치 지정
fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/batang.ttc'
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

print("리뷰의 최대 길이 : {:,}".format(max(len(l) for l in x_train_encoded)))
print("리뷰의 평균 길이 : {:,.2f}".format(sum(map(len, x_train_encoded))/len(x_train_encoded)))

plt.hist([len(s) for s in x_train_encoded], bins=50)
plt.xlabel("리뷰 길이")
plt.ylabel("리뷰 갯수")
plt.show()


# 리뷰 최대 길이 선정
max_len = 50
cnt = 0
for s in x_train_encoded:
    if len(s) <= max_len:
        cnt = cnt + 1
print("리뷰 길이가 {} 이하인 비율: {:.8f}%".format(max_len, (cnt / len(x_train_encoded))*100))


# 패딩 처리
x_train_padded = pad_sequences(x_train_encoded, maxlen = max_len)
x_test_padded = pad_sequences(x_test_encoded, maxlen = max_len)


# 패딩 처리된 데이터 저장
## 유닉스에서는 확장자의 의미가 없긴함 npy 안적어도 됨
## 윈도우나 의미 있지 
np.save("../99.data/NaverMovieReview/x_train_padded.npy", x_train_padded, allow_pickle=True)
np.save("../99.data/NaverMovieReview/x_test_padded.npy", x_test_padded, allow_pickle=True)