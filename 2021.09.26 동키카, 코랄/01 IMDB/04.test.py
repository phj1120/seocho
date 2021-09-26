import re
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# 단어 집합
word_index = imdb.get_word_index()
index_to_word = {}
for key, value in word_index.items():
    index_to_word[value + 3] = key
index_to_word[0] = "<pad>"
index_to_word[1] = "<sos>"
index_to_word[2] = "<unk>"

# 모델 불러오기
loaded_model = load_model("../models/imdb/best_model_LSTM.h5")

def predict_text(text):
    # 알파벳과 숫자를 제외하고 모두 제거 및 알파벳 소문자화
    sentence = re.sub('[^0-9a-zA-Z ]', '', text).lower()

    # 정수 인코딩
    encoded = []

    for word in sentence.split():
        # 10,000개로 학습 했기 때문에 단어 집합의 크기를 10,000으로 제한
        try:
            if word_index[word] <= 10000:
                encoded.append(word_index[word] + 3)
            else:
                # 10,000 이상의 숫자는 <unk> 토큰으로 취급
                encoded.append(2)
        # 단어 집합에 없는 단어는 <unk> 토큰으로 취급
        except KeyError:
            encoded.append(2)
    print(encoded)
    # 패딩
    max_len = 500
    padding = pad_sequences([encoded], maxlen=max_len)

    # 예측
    score = float(loaded_model.predict(padding))

    if score > 0.5:
        print("{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100))


# 예측 데이터
neg_text = "This movie was just way too overrated. The fighting was not professional and in slow motion. I was expecting more from a 200 million budget movie. The little sister of T.Challa was just trying too hard to be funny. The story was really dumb as well. Don't watch this movie if you are going because others say its great unless you are a Black Panther fan or Marvels fan."
predict_text(neg_text)

pos_text = "I was lucky enough to be included in the group to see the advanced screening in Melbourne on the 15th of April, 2012. And, firstly, I need to say a big thank-you to Disney and Marvel Studios. Now, the film... how can I even begin to explain how I feel about this film? It is, as the title of this review says a 'comic book triumph'. I went into the film with very, very high expectations and I was not disappointed. Seeing Joss Whedon's direction and envisioning of the film come to life on the big screen is perfect. The script is amazingly detailed and laced with sharp wit a humor. The special effects are literally mind-blowing and the action scenes are both hard-hitting and beautifully choreographed."
predict_text(pos_text)