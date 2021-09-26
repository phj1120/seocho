# 2021.09.26
## 코드 설명
### 01 IMDB
* tensorflow.keras.datasets 를 이용해 데이터셋 로드해 간단하게 과정 숙지
* tensorflow.keras.callbacks 의 EarlyStopping, ModelCheckpoint 을 이용해 모델 학습

### 02 IMDB_TF_HUB
* tensorflow_hub 이용해 훈련

### 03 NaverMovie
* 네이버 영화 리뷰 감성 분류
* 단순 크롤링 된 데이터를 이용해 데이터 전처리 부터 학습 까지 진행

#### 학습 과정
1. 중복 데이터 제거
2. 비어있는(Null) 데이터 제거
3. 한글 이외의 문자 제거
4. 의미없는 데이터(불용어,  stopword)
5. 토큰화(형태소 분석)
6. 정수인코딩(워드 사전처리)
7. 패딩
8. 학습

#### 예측 과정
1. 모델
2. 토큰화(mecab)
3. 불용어 처리
4. 정수 인코딩
5. 패딩
6. 예측

### 04.NaverShopping
* 네이버 쇼핑 감성 분석
* 네이버 영화 감성 분석과 전체적인 흐름 동일

### 05.Flask
모델을 만들어서 Flask로 웹 서비스 해볼 예정

* Django / 규모가 크고 좋지만, 틀에 갖혀있는 느낌

* Flask / 자유도가 높지만, 별도로 설치 및 구현해야함 

Django가 틀에 갖혀있지만 적응하면 되게 편함 다른거 못써..

Flask 는 다른거 쓰기 편함

-> Django 하기전에 Flask 해보자



# 다음시간 
1. rasa 
2. kochat

추가로 할것
* https://i.kakao.com/
* kakao i open builder
* 신청 후 사용 6일 이내에 사용가능

