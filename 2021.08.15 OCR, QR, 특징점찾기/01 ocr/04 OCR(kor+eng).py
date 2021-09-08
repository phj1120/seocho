from PIL import Image     #pip install pillow
from pytesseract import * #pip install pytesseract
import configparser
import os

start_path = 'img'
file_name = f'{start_path}/test.png'
outTxtPath = f'{start_path}/result.txt'

img = Image.open(file_name)
outText = image_to_string(img, lang='kor+eng', config='--psm 1')

with open(outTxtPath, 'w', encoding='utf-8') as f:
    f.write(outText)
print(outText)

#추출(이미지파일, 추출언어, 옵션)
#preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인한다.
#psm(페이지 세그먼트 모드 : 이미지 영역안에서 텍스트 추출 범위 모드)
#psm 모드 : https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage

