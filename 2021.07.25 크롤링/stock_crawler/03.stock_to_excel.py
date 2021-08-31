"""
주식정보를 가져와서 엑셀에 저장
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1

1. 패키지 설치
pip install tqdm
pip install beautifulSoup4
pip install requests
pip install numpy
pip install pandas
pip install lxml
pip install openpyxl
"""

import os
import requests
import numpy as np
import pandas as pd
from tqdm import tqdm
from datetime import datetime
from bs4 import BeautifulSoup as bs


# 종목정보 가져오기
def get_stock(sosok):
    # 마지막 페이지
    page_url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=' + str(sosok) + '&page=1'
    page_res = requests.get(page_url)
    page_soup = bs(page_res.text, 'html.parser')
    last_page = page_soup.select_one('td.pgRR > a').get('href').split('=')[-1]

    # 정보를 담을 DataFrame
    sise_df = pd.DataFrame()
    for page in tqdm(range(1, int(last_page) + 1, 1)):
        target_url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=' + str(sosok) + '&page=' + str(page)
        target_res = requests.get(target_url)
        target_soup = bs(target_res.text, 'html.parser')
        table = target_soup.select_one('div.box_type_l')

        # 칼럼
        data_header = [item.get_text().strip() for item in table.select('thead th')][1:-1]
        data_header.append('토론실')

        # 종목 정보
        data_item = [item.get_text().strip() for item in table.find_all(
            lambda x: (x.name == 'a')
            or (x.name == 'td' and 'number' in x.get('class', []))
        )]

        # 코스닥, 코스피 제거
        if sosok == 0:
            data_item.remove('코스닥')
        else:
            data_item.remove('코스피')

        # 종목 순번
        data_no = [item.get_text().strip() for item in table.select('td.no')]

        # 행렬로 변환
        data_np = np.array(data_item)
        data_np.resize(len(data_no), len(data_header))

        # 기존 DataFrame과 합치기
        sise_df = pd.concat([sise_df, pd.DataFrame(data=data_np, columns=data_header)])
    return sise_df


if __name__ == '__main__':
    # 디렉터리 생성
    pwd = os.getcwd()
    image_directory = os.path.join(pwd, "일별시세")

    try:
        if not os.path.exists(image_directory):
            os.makedirs(image_directory)
    except OSError:
        print('디렉터리 생성 실패')

    kospi = get_stock(0)  # 코스피
    kosdaq = get_stock(1)  # 코스닥

    # 코스피, 코스닥 정보를 하나로 합치기
    sise = pd.concat((kospi, kosdaq), axis=0, ignore_index=True)

    # 토론실 제거
    sise = sise.iloc[:, :-1]

    # 엑셀로 저장
    today = datetime.today().strftime('%Y-%m-%d')
    sise.to_excel(os.path.join('일별시세', '{}.xlsx'.format(today)))
