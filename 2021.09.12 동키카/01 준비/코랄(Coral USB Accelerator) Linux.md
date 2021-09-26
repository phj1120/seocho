# 1. Edge TPU runtime 설치

## 1.1 시스템에 패키지 추가

```bash
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update
```

## 1.2 Edge TPU runtime 설치

```bash
# 성능 보통
sudo apt-get install libedgetpu1-std

# 성능 최고
sudo apt-get install libedgetpu1-max
```

## 1.3 코랄 연결

- 더 빠른 속도를 원한다면  USB 3.0 (파란색)에 연결

# 2. PyCoral 라이브러리 설치

## 2.1 설치

```bash
sudo apt-get install python3-pycoral
```

## 2.2 필요 파일 다운로드

```bash
bash examples/install_requirements.sh classify_image.py
```

## 2.3 인터프리터 변경

```bash
pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl
```

## 2.4 이미지 분류 실행

```bash
python3 examples/classify_image.py --model test_data/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite --labels test_data/inat_bird_labels.txt --input test_data/parrot.jpg
```

- 라벨의 신뢰도 0.0 ~ 1.0 사이로 출력

# 참고 사이트

[https://coral.ai/docs/accelerator/get-started/](https://coral.ai/docs/accelerator/get-started/)