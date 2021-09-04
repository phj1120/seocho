# 최종 목적 : 얼굴 감별기 만들기

### 설계

1. 연애인 얼굴 감별해 보자

2. 런닝맨 출연진의 얼굴을 감별해보자

3. 런닝맨 출연진 명단 확보(5명)

- https://namu.wiki/w/%EB%9F%B0%EB%8B%9D%EB%A7%A8

- 지석진, 유재석, 김종국, 하하, 양세찬

4. 데이터셋 

- 크롤링으로 이미지를 확보

- 01.crawling.py

6. 얼굴 이미지만 잘라내기

- face_recognition 모듈을 이용해서 얼굴만 잘라내서 저장하기

- 02.cropping.py

7. 필터링

(1) 대상이 아닌 얼굴 제거

- 대표 얼굴 사진 선정

- 나머지 사진들을 대표 얼굴 사진과 비교해서 distance 0.8 이상 차이가 나면 해당파일을 삭제

- 참고 : https://github.com/ageitgey/face_recognition/blob/master/examples/face_distance.py

(2) 중복데이터 제거

- 03.filtering.py

8. 데이터셋 분류 

- 학습 : 70%

- 테스트 : 30% 

- 04.dividing.py

10. 학습 => 모델 (VGG Face)

- 05.training.py


9. 검증

- 06.testing.py

### 패키지

```shell
conda install -c conda-forge selenium
conda install -c conda-forge face_recognition
pip install shutils
pip install tensorflow
```

### 크롬드라이버

- https://chromedriver.chromium.org/downloads