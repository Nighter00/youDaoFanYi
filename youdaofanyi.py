from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def upWord():
    wait = WebDriverWait(driver, 10)
    input_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#inputOriginal')))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#transMachine')))
    for key in key_word:
        time.sleep(0.1)
        input_bar.send_keys(key)
    submit.click()


def get_word():
    wait = WebDriverWait(driver, 10)
    word_bar = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#transTarget > p:nth-child(1) > span:nth-child(1)')))
    return word_bar.text


def main():
    driver.get(url)
    upWord()
    print("翻译结果:" + get_word())


if __name__ == '__main__':
    headers = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument(headers)
    options.add_argument('disable-infobars')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    url = 'http://fanyi.youdao.com/'
    key_word = input("输入查询单词：")
    main()
    driver.quit()
