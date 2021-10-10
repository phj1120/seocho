1. raw data
    -> 데이터 셋
        자료마다 변수명이 다 달라 일관되게 사용하는 것이 좋음
        - x_train   (검증 데이터)
        - y_train   (학습 라벨, 정답)
        - x_test    (검증 데이터)
        - y_test    (검증 라벨)
    -> 7 : 3 의 비율
        데이터가 적을 경우 의미 없음

    csv로 데이터를 처리하는 것이 좋음
        -> pandas dataframe 이용하는 것이 가장 용이
        -> numpy
    matplotlib

2. 토큰화
    -> 영어
        -> space로 단어 분리

    -> 한글
        -> 띄어쓰기 없음
        -> 형태소 분석 : KoNLPy 라이브러리 Kkma, Komoran, Hannanum, Okt, Mecab
           시간 차이는 많이 나지만 정확도는 크게 차이 없었음

3. 정수 인코딩
    -> 단어 사전(word index) 만들어 사용

4. 패딩
    -> 글자수 맞춰 줌

5. 학습
    -> GRU, LSTM, BiLSTM
    이 순서대로 다 해보는 것이 좋음

형태소 분석기 라이브러리 Mecab 설치 방법에 따라 훈련 다르게 하기
토큰화 결과가 달라서 코드 개인 수정 필요(vocab_size)

eunjeon 기준으로 작성