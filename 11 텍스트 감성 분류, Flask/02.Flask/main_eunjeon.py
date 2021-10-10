# pip install eunjeon
# visual studio build tool 14.0 필요

# set FLASK_APP = main 윈도우
#  FLASK_APP = main 윈도우

# flask run
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from eunjeon import Mecab

from flask import Flask, render_template, jsonify, request

x_train_tokenized = np.load("../99.data/NaverShoppingReview/x_train_tokenized.npy", allow_pickle=True)
stopwords = ["도", "는", "다", "의", "가", "이", "은", "한", "에", "하", "고", "을", "를", "인", "듯", "과", "와", "네", "들", "듯", "지",
             "임", "게"]
model = load_model("../98.models/NaverShoppingReview/best_model_GRU.h5")
# model = load_model("../98.models/NaverShoppingReview/best_model_LSTM.h5")

mecab = Mecab()

vocab_size = 21022
tokenizer = Tokenizer(vocab_size, oov_token="OOV")
tokenizer.fit_on_texts(x_train_tokenized)

app = Flask(__name__)


def predict(text):
    tokenized = mecab.morphs(text)
    tokenized = [word for word in tokenized if not word in stopwords]
    encoded = tokenizer.texts_to_sequences([tokenized])
    padded = pad_sequences(encoded, maxlen=80)
    score = float(model.predict(padded))
    return score


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/inference", methods=["POST"])
def inference():
    text = request.form["text"]
    # 추론
    text_score = predict(text)

    print(f"text: {text} score : {text_score}")
    return jsonify(
        score=text_score,
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)