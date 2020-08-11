from selenium import webdriver
import pandas as pd
from selenium.webdriver import ActionChains
import time, random


def get_track(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 10
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path="D:/code/MoonSpider/drivers/chromedriver.exe")
    browser.get("https://www.qichacha.com/")
    browser.get_cookies()
    j = 0
    browser.get("https://www.qichacha.com/firm_859cfa33bffc6825f53b2af63d6ac466.html")
    action = ActionChains(browser)
    but = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")
    action.click_and_hold(but).perform()
    track_list = get_track(200 + 3)
    for track in track_list:
        action.move_by_offset(xoffset=track, yoffset=0).perform()
        action.reset_actions()

    imitate = action.move_by_offset(xoffset=-1, yoffset=0)
    time.sleep(0.015)
    imitate.perform()
    time.sleep(random.randint(6, 10) / 10)
    imitate.perform()
    time.sleep(0.04)
    imitate.perform()
    time.sleep(0.012)
    imitate.perform()
    time.sleep(0.019)
    imitate.perform()
    time.sleep(0.033)

    action.move_by_offset(xoffset=1, yoffset=0).perform()
    # 放开圆球
    action.pause(random.randint(6, 14) / 10).release().perform()
    time.sleep(2)
    # 务必记得加入quit()或close()结束进程，不断测试电脑只会卡卡西
    h = 1
    browser.close()
