import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from eunjeon import Mecab


# 데이터 로드
x_train_tokenized = np.load("../99.data/NaverMovieReview/x_train_tokenized.npy", allow_pickle=True)

# 형태소 분석기
mecab = Mecab()

vocab_size = 28631
tokenizer = Tokenizer(vocab_size, oov_token = 'OOV')
tokenizer.fit_on_texts(x_train_tokenized)

# 불용어
stopwords = ["도", "는", "다", "의", "가", "이", "은", "한", "에", "하", "고", "을", "를", "인", "듯", "과", "와", "네", "들", "듯", "지", "임", "게"]

# 모델 불러오기
loaded_model = load_model("../98.models/NaverMovieReview/best_model_GRU.h5")
# loaded_model = load_model("../98.models/NaverMovieReview/best_model_LSTM.h5")

# 최대 길이 지정
max_len = 50

def predict(text):
    # 전처리
    tokenized = mecab.morphs(text) # 토큰화
    tokenized = [word for word in tokenized if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([tokenized]) # 정수 인코딩
    padded = pad_sequences(encoded, maxlen = max_len) # 패딩
    score = float(loaded_model.predict(padded)) # 예측
    if score > 0.5:
        print("{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100))

# 확인
## 긍정
predict("이 영화 개꿀잼 ㅋㅋㅋ")
## 부정
predict("감독 뭐하는 놈이냐?")