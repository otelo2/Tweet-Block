from selenium import webdriver
from secrets import username,password
from time import sleep
class TweetBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.login()
        self.block_demo()

    def login(self):
        self.driver.get('https://twitter.com')

        sleep(4)

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
        print("User blocked")
        sleep(1)

    #User needs to be blocked for this to work
    def unblock(self):
        unblock_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div')
        unblock_btn.click()
        sleep(1)
        confirm_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]')
        confirm_btn.click()
        print("User unblocked")
        sleep(1)

    #This just selects the first acc that pops up, for demo purposes
    def select_victim(self):
        victim_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div[1]')
        victim_text = victim_btn.text
        print("Victim: ",victim_text)
        victim_btn.click()
        sleep(1)

    def go_home(self):
        home_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[1]/h1/a')
        home_btn.click()
        sleep(1)

    #Needs to be first in the following list
    def get_user_text(self, victim_btn):
        #victim_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div[1]')
        victim_text = victim_btn.text
        victim_data = victim_text.split("\n")
        print("Name: ",victim_data[0])
        print("Handle: ",victim_data[1])
        print("Status: ", victim_data[2])
        print("Bio: ", victim_data[3])
        print("-------------")

    def user_list_selection(self):
        for num in range(1,10):
            victim_btn = self.driver.find_element_by_xpath(f'//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div[{num}]')
            print(f'{num}.-')
            self.get_user_text(victim_btn)

    def block_demo(self):
        self.search()
        self.getFollowing()
        self.user_list_selection()
        #self.get_user_text()
        #self.select_victim()
        #self.block()
        #self.go_home()