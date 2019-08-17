from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot():
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password
    
    def Login(self):
        browser = self.browser
        browser.get('https://twitter.com/')
        time.sleep(3)
        btn = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[1]/a')
        btn.click()
        time.sleep(3)
        _uname = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input')
        _uname.clear()
        _uname.send_keys(self.username)
        pwd = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input')
        pwd.clear()
        pwd.send_keys(self.password)
        login_btn = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button')
        login_btn.click()
        time.sleep(3)


bot = TwitterBot('username', 'password')
bot.Login()