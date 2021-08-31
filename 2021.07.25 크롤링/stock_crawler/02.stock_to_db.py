"""
주식정보를 가져와서 데이터베이스에 저장
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1

1. 패키지 설치
pip install pymysql
pip install tqdm
pip install beautifulSoup4
pip install requests

2. 크롬드라이버
https://chromedriver.chromium.org/downloads
"""

import pymysql
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs


# 데이터베이스 연결
def connect_db():
    db = pymysql.connect(
        user='seocho',
        passwd='gqWZ0f9OkV1Mn1qj',
        host='jeongps.com',
        db='seocho',
        charset='utf8'
    )
    return db


# 테이블 생성
def create_table(db):
    curs = db.cursor(pymysql.cursors.DictCursor)
    sql = '''CREATE TABLE IF NOT EXISTS `TB_STOCK` (
        `CODE` varchar(10) NOT NULL PRIMARY KEY,
        `NAME` varchar(50) NOT NULL
    );'''
    curs.execute(sql)
    db.commit()


# 데이터 저장
def save_to_db(code, name, db):
    sql = '''INSERT INTO `TB_STOCK` (CODE, NAME) VALUES (%s, %s)'''
    curs = db.cursor(pymysql.cursors.DictCursor)
    curs.execute(sql, (code, name))
    db.commit()


# 종목정보 가져오기
def get_stock(sosok, db):
    # 마지막 페이지
    page_url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=' + str(sosok) + '&page=1'
    page_res = requests.get(page_url)
    page_soup = bs(page_res.text, 'html.parser')
    last_page = page_soup.select_one('td.pgRR > a').get('href').split('=')[-1]

    for page in tqdm(range(1, int(last_page) + 1, 1)):
        target_url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=' + str(sosok) + '&page=' + str(page)
        target_res = requests.get(target_url)
        target_soup = bs(target_res.text, 'html.parser')
        tbody = target_soup.select_one('tbody')
        trs = tbody.find_all('tr', attrs={'onmouseover': 'mouseOver(this)'})

        for tr in trs:
            href = tr.find_all('a')
            name = href[0].text
            code = href[0].get('href').split('=')[-1]

            # 데이터 저장
            save_to_db(code, name, db)


if __name__ == '__main__':
    db = connect_db()
    create_table(db)
    get_stock(0, db)  # 코스피
    get_stock(1, db)  # 코스닥
    db.close()
