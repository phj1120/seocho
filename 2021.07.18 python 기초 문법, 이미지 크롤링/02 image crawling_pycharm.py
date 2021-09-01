import time, urllib, uuid, os, sys

from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
content = input('수집할 이미지 입력 : ')
elem.send_keys(content)
elem.send_keys(Keys.RETURN)

path = f'img/{content}'

try:
  if not os.path.exists(path):
    os.makedirs(path)

except OSError:
  print('Error : Creating directory.' + path)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

count = 1
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
for image in images:
    try:
        image.click()
        # time.sleep(1)
        imgUrl = driver.find_element_by_xpath(
            '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute(
            "src")
        file_name = uuid.uuid4()
        file_path = f'{path}/{file_name}.jpg'
        urllib.request.urlretrieve(imgUrl, file_path)
        print(f'Saving {count}: {file_path}')
        count += 1
    except:
        pass