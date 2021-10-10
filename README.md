# 서초구 로봇 코딩 칼리지 - 고급반

## 보조강사 하며 느낀점 (2021.10.10.)

수강생분들이 뛰어나신 분들이 많으셔서, 과연 내가 이 자리에 있어도 될까? 라는 생각이 많이 들었습니다.

하지만 그 수강생분들 덕분에 보조 강사로서 해야 할 역할을 제대로 하기 위해 더 열심히 준비할 수 있었습니다.

그 과정에서 제 마음을 들여다보고, 앞으로 어떻게 살아야 할지 고민하는 기회가 되었습니다.

또 각자만의 분야에서 열심히 사는 사람들을 보며 나도 저렇게 되고 싶다. 저렇게 되기 위해 꾸준히 노력해야겠다는 생각이 들었습니다.

그러기 위해 어제는 바꿀 수 없지만, 내일은 바꿀 수 있다는 생각으로 오늘을 살아가겠습니다.


## 수업 구성
### 1주차(2021.07.18.)
* python 기초 문법
* 이미지 크롤링

### 2주차(2021.07.25.)
* 이미지 크롤링
* 주식 정보 크롤링
* 딥러닝 실습

### 3주차(2021.08.01.)
* 런닝맨 출연진 얼굴 인식
* 얼굴 추출 
* 얼굴 인식
* 필터링

### 4주차(2021.08.08.)
* 구글 비전 API

### 5주차(2021.08.15.)
* OCR, QR code
* 번호판 인식
* 특징점 찾기

### 6주차(2021.08.22.)
* 라즈베리파이 기초

### 7주차(2021.08.29.)
* 라즈베리파이 활용
* 카메라에 찍히는 색에 맞춰 LED 켜기(opencv, custom_model)
* 라즈베리파이 프로젝트 - 주차 감지기(초음파센서, 부저, LED)
* 카메라에 찍히는 숫자 LCD에 표시(openCV, MNIST)

### 8주차(2021.09.05.)
* 라즈베리파이 프로젝트 - 체온 측정(초음파센서, 비접촉식온도센서, LED, 부저, LCD)
* 데이터 베이스 (sqlite, pymysql)

### 9주차(2021.09.12.)
* 동키카 
* 동키카 시뮬레이터

### 10주차(2021.09.26.)
* 텍스트 감성 분류(IMDB, 네이버 영화 리뷰)

동키카와 코랄을 이용해 자율주행을 더 진행할 예정이었으나 

제한사항(네트워크 환경)이 생겨 감성 분류 웹, 앱 교육 진행

### 11주차(2021.10.03.)
* 텍스트 감성 분류(네이버 쇼핑) 웹 제작(FLASK)

### 12주차(2021.10.10.)
* 텍스트 감성 분류 앱 제작(Flutter)


## 파이썬 환경 구성
### PC
```bash
windows 10 64bit
python 3.8
pip install -r requirements.txt
```
### 라즈베리파이
#### 1. Tensorflow

```bash
pip3 install --upgrade https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl
```

#### 2. tflite Interpreter
```bash
pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
```

#### 3. OpenCV
```bash
sudo apt-get update && upgrade
# sudo apt-get install python3-dev, libatlas-base-dev, libhdf5-dev, libhdf5-serial-dev
sudo apt-get install python3-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libhdf5-dev 
sudo apt-get install libhdf5-serial-dev
pip3 install opencv-contrib-python
pip3 install -U numpy
```