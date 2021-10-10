import os
import time
import urllib
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys

# 96.chromedriver 불러오기
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('96.chromedriver/92.0.4515.107/chromedriver', options=chrome_options)
# driver = webdriver.Chrome('96.chromedriver/92.0.4515.107/chromedriver_mac64', options=chrome_options)
#driver = webdriver.Chrome('../96.chromedriver/92.0.4515.107/chromedriver_mac64_m1', options=chrome_options)

# 디렉터리 생성
pwd = os.getcwd()
image_directory = os.path.join(pwd, "crawling_images")
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# 츨연진
names_kor = ['하동훈', '지석진', '김종국', '양세찬', '유재석']
names_eng = ['Ha Dong Hoon', 'Ji Seok Jin', 'Kim Jong-kook', 'Yang Se-chan', 'Yoo Jae-suk']

# 출연진 명단을 통해서 한명식 이미지를 클롤링
for i, name in enumerate(names_kor):
    print(f'[{name}] 이미지 크롤링 시작')

    # 이름 디렉터리 생성
    name_directory = os.path.join(pwd, "crawling_images", names_eng[i])
    if not os.path.exists(name_directory):
        os.makedirs(name_directory)

    # 이미지 크롤링
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    query = driver.find_element_by_name("q")
    query.send_keys(name)
    query.send_keys(Keys.RETURN)

    # 이미지를 최대로 찾기 위해서 스크롤을 계속 아래로 내림
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        print(f"[{name}] 이미지를 최대로 찾기 위해서 스크롤을 아래로 내리는 중")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break

        last_height = new_height

    # 이미지 태그 클래스
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    # 이미지 다운로드
    count = 1
    for image in images:
        try:
            image.click()
            image_url = driver.find_element_by_xpath(
                "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img").get_attribute(
                "src")

            # 이미지 저장
            urllib.request.urlretrieve(image_url, f"{name_directory}/{count}.jpg")
            print(f"[{name}] {count}개 저장완료")
            count = count + 1
        except:
            pass

        # if count > 100:
        #     break

    print(f"[{name}] 다운로드 완료")
