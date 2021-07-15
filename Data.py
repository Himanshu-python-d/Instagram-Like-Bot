from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import smtplib


search_query = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver = webdriver.Chrome(
    executable_path='C:\\Users\pc\Downloads\chromedriver.exe')
driver.get(search_query)
time.sleep(5)
driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('Praffulbisen')

driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('Prafful@123')

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(3)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(3)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('himanshuyadav111')
time.sleep(3)
driver.find_element_by_class_name('-qQT3').click()
time.sleep(2)

posts = driver.find_elements_by_class_name('eLAPa')

for post in range(len(posts)):
    posts[post].click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
    time.sleep(2)
    close_button = driver.find_element_by_xpath(
        '/html/body/div[5]/div[3]/button').click()
    time.sleep(2)
time.sleep(50)
driver.quit()
