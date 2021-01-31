from selenium import webdriver
import time
import requests 
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def METPULL(code):

    ##code should be a string

    driver = webdriver.Chrome('/Users/toprak/Desktop/Kodlar/DGANS/chromedriver')


    url  = 'https://www.metmuseum.org/search-results#!/search?q='+code

    driver.get(url)

    timeout = 20
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div/img'))
        WebDriverWait(driver, timeout).until(element_present)

        photo = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div/img')
        photo.click()

    except TimeoutException:
        print("Timed out waiting for page to load")

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="the-artwork__inset"]/figure/div[2]/ul/li[2]/a'))
        WebDriverWait(driver, timeout).until(element_present)

        download = driver.find_element_by_xpath('//*[@id="the-artwork__inset"]/figure/div[2]/ul/li[2]/a')
        download.click()

    except TimeoutException:
        print("Timed out waiting for page to load")

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/img'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:
        print("Timed out waiting for page to load")


    photolink = driver.current_url
    print(photolink)
    response = requests.get(photolink)

    file = open(photolink.split('/')[-1], "wb")
    file.write(response.content)
    file.close()

    driver.quit()


METPULL('1975.1.1992')
METPULL('60.708(117)')
METPULL('17.50.7')
METPULL('22.73.3(80-81')
