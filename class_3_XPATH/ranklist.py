from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import cv2 as cv
import numpy as np
import time

url='https://www.holiday.com.tw/SongInfo/SongList.aspx?st=top&lt=tc'
if __name__=='__main__':
    service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service)
    #driver=webdriver.Chrome()
    driver.get(url)
    wait=WebDriverWait(driver, 10)
    # 爬到所有歌
    songs=wait.until(EC.presence_of_all_elements_located((By.XPATH, "__???__")), "Error")
    for song in songs:
        print(song.text)