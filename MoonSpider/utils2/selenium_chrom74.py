from selenium import webdriver

import time

if __name__=='__main__':

    browser = webdriver.Chrome(executable_path="D:/code/MoonSpider/drivers/chromedriver.exe")
    time.sleep(3)
    browser.get("https://www.qichacha.com/")
    time.sleep(5)
    cookies = browser.get_cookies()
    for c in cookies:
        print(c)
