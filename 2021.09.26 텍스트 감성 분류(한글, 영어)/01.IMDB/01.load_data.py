import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb

(x_train, y_train), (x_test, y_test) = imdb.load_data()
print('훈련 데이터 : {:,}개'.format(len(x_train)))
print('검증 데이터 : {:,}개'.format(len(x_test)))
print(x_train[0])

word_index = imdb.get_word_index()
print(word_index)
print('word_index : {:,}개'.format(len(word_index)))

# word_index value 1부터 시작
# sorted(word_index.values())

index_to_word = {}
# json 형태이므로 키, 값으로 뽑아줌
for key, value in word_index.items():
    # 0은 원래 비어 있으니까 + 2만 해줘도 될거같은데..
    # ? +3 0, 1, 2 는 특별한 의미를 같은 데이터로 받을거라
    # print(key, value)
    index_to_word[value + 3] = key

index_to_word[0] = "<pad>"
index_to_word[1] = "<sos>"
index_to_word[2] = "<unk>"

# print(index_to_word[3])
# index_to_word[3]의 값이 비어있어서 3이 포함된 범위는 전체 출력 안됨
print(index_to_word)

# 인덱스를 원래 단어로 매칭
print(" ".join([index_to_word[index] for index in x_train[0]]))