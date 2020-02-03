from selenium import webdriver
from secrets import username,password
from time import sleep

class TweetBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://twitter.com')

        sleep(10)

        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
        login_btn.click()

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input')
        email_in.send_keys(username)
        pass_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input')
        pass_in.send_keys(password)
        send_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
        send_btn.click()

    def search(self):
        a=1