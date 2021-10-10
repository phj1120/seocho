## dlib 사용을 위해 콘다 환경에서 해야함

```bash
pip install tqdm
pip install beautifulSoup4
pup install requests
pip insatll numpy
pipinstall pandas

conda install -c conda-forge face_recognition
```

# 최종 목적 : 얼굴 감별기

1. 연애인 얼굴 감별
2. 런닝맨 출연진 얼굴 감별
3. 런닝맨 출연진 명단 확보
4. 데이터셋 -> 크롤링으로 해결
5. 얼굴 이미지만 잘라내기
6. 필터링
(1) 대상 아닌 얼굴 제거
(2) 중복 데이터 제거
7. 학습 -> 모델 (VGG Face)
8. 검증