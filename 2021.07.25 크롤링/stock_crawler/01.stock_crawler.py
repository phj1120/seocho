"""
주식정보를 가져와서 데이터베이스에 저장
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1

1. 패키지 설치
pip install beautifulSoup4
pip install requests
"""

import requests
from bs4 import BeautifulSoup as bs


# 종목정보 가져오기
def get_stock(sosok):
    # 마지막 페이지
    page_url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=' + str(sosok) + '&page=1'
    page_res = requests.get(page_url)
    page_soup = bs(page_res.text, 'html.parser')
    last_page = page_soup.select_one('td.pgRR > a').get('href').split('=')[-1]

    for page in range(1, int(last_page) + 1, 1):
        target_url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=' + str(sosok) + '&page=' + str(page)
        target_res = requests.get(target_url)
        target_soup = bs(target_res.text, 'html.parser')
        tbody = target_soup.select_one('tbody')
        trs = tbody.find_all('tr', attrs={'onmouseover': 'mouseOver(this)'})

        for tr in trs:
            href = tr.find_all('a')
            name = href[0].text
            code = href[0].get('href').split('=')[-1]
            print(name, code)


if __name__ == '__main__':
    get_stock(0)  # 코스피
    get_stock(1)  # 코스닥
