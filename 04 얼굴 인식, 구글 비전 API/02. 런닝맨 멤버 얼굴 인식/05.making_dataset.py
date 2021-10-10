import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import ZeroPadding2D, Convolution2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten, Activation, BatchNormalization
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input
import tensorflow.keras.backend as K
from keras_preprocessing.image import ImageDataGenerator

import autokeras as ak

# 학습용 데이터셋 준비하기
member_name_path = 'datasets/train'
member_name_list = os.listdir(member_name_path)

x_train = []
y_train = []
    
for i, name in enumerate(member_name_list):
    member_imgs_path = os.path.join(member_name_path, name)
    member_imgs = os.listdir(member_imgs_path)
    for member_img in member_imgs:
        img_path = os.path.join(member_imgs_path, member_img)
        # print(img_path, i)
        img = cv2.imread(img_path, 0)
        img = cv2.resize(img, dsize = (28, 28))
        x_train.append(img)
        y_train.append(i)

x_train = np.array(x_train)
y_train = np.array(y_train)

print('x_train : ', x_train.shape)
print('y_train : ', y_train.shape)

  # 테스트용 데이터셋 준비하기
member_name_path = 'datasets/test'
member_name_list = os.listdir(member_name_path)

x_test = []
y_test = []
    
for i, name in enumerate(member_name_list):
    
    member_imgs_path = os.path.join(member_name_path, name)
    member_imgs = os.listdir(member_imgs_path)
    for member_img in member_imgs:
        img_path = os.path.join(member_imgs_path, member_img)
        # print(img_path, i)
        ori_img = cv2.imread(img_path, 0)
        ori_img = cv2.resize(ori_img, dsize = (28, 28))

        x_test.append(ori_img)
        y_test.append(i)

x_test = np.array(x_test)
y_test = np.array(y_test)

print('x_test :  ', x_test.shape)
print('y_test :  ' , y_test.shape)


# Save test and train data for later use
np.save('train_data', x_train)
np.save('train_labels', y_train)
np.save('test_data', x_test)
np.save('test_labels', y_test)

print("데이터셋 생성 완료")