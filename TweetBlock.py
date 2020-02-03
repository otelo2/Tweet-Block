from selenium import webdriver
from secrets import username,password
from time import sleep

class TweetBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://twitter.com')

        sleep(5)

        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
        login_btn.click()

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input')
        email_in.send_keys(username)
        pass_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input')
        pass_in.send_keys(password)
        send_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
        send_btn.click()
        print("Logged in")

    def search(self):
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        search_bar.send_keys('@ennioft')
        sleep(0.5)
        try:
            user_result = self.driver.find_element_by_xpath('//*[@id="typeaheadDropdown-5"]/div[3]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div[1]/span/span')
            user_result.click()
        except Exception:
            #Ugly fix for now
            self.driver.get('https://twitter.com/ennioft')
            print("Used alternative search")

    def getFollowing(self):
        following_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[2]/span')
        following_btn.click()
