from selenium import webdriver
from secrets import username,password
from time import sleep

class TweetBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.login()

    def login(self):
        self.driver.get('https://twitter.com')

        sleep(5)

        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
        login_btn.click()

        sleep(1)

        email_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input')
        email_in.send_keys(username)
        pass_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input')
        pass_in.send_keys(password)
        send_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
        send_btn.click()
        print("Logged in")
        sleep(1)

    def search(self):
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        search_bar.send_keys('@ennioft')
        sleep(6)
    #    try:
    #        user_result = self.driver.find_element_by_xpath('//*[@id="typeaheadDropdown-2"]/div[3]/div[2]/div/span')
    #        user_result.click()
    #    except Exception:
    #        #Ugly fix for now
    #        self.driver.get('https://twitter.com/ennioft')
    #        print("Used alternative search")
        try:
            print('Try 1')
            user_result = self.driver.find_element_by_xpath('//*[@id="typeaheadDropdown-2"]/div[3]/div[2]/div/span')
            user_result.click()
        except Exception:
            try:
                print('Try 2')
                user_result = self.driver.find_element_by_xpath('//*[@id="typeaheadDropdown-2"]/div[3]/div[1]/div/div[1]')
                user_result.click()
            except Exception:
                print('Try 3')
                user_result = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[3]/div[1]')
                user_result.click()
        print('Ended search')
        sleep(2)

    def getFollowing(self):
        following_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[2]/span')
        following_btn.click()
        sleep(1)

    def test(self):
        self.search()
        self.getFollowing()

    def block(self):
        more_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div')
        more_btn.click()
        sleep(1)
        block_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div[3]')
        block_btn.click()
        sleep(1)
        confirm_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]')
        confirm_btn.click()
        sleep(1)

    def unblock(self):
        unblock_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div')
        unblock_btn.click()
        sleep(1)
        confirm_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]')
        confirm_btn.click()
        sleep(1)

