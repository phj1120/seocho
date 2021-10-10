import cv2
import numpy as np
import autokeras as ak
import matplotlib.pyplot as plt

# # 데이터 불러오기
x_train = np.load('train_data.npy')
y_train = np.load('train_labels.npy')
x_test = np.load('test_data.npy')
y_test = np.load('test_labels.npy')
print('데이터셋 로드 완료')

# ImageClassifier 선언
clf = ak.ImageClassifier(overwrite=True, max_trials=5)
# clf = ak.ImageClassifier(overwrite=True)

# 이미지를 이용해 훈련
clf.fit(x_train, y_train, epochs=100)

# 최적의 모델로 예측
predicted_y = clf.predict(x_test)

# 테스트 데이터로 최적의 모델 평가
print(clf.evaluate(x_test, y_test))

member_name = ['Ha Dong Hoon', 'Ji Seok Jin', 'Kim Jong-kook', 'Yang Se-chan', 'Yoo Jae-suk']
test_numbers = np.random.randint(len(x_test), size = 25)

plt.figure(figsize=(10,10))
for i, test_number in enumerate(test_numbers):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(cv2.cvtColor(x_test[test_number], cv2.COLOR_BGR2RGB))
    plt.xlabel(member_name[int(predicted_y[test_number][0])])
plt.show()