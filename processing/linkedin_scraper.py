from selenium import webdriver
from bs4 import BeautifulSoup as soup
from getpass import getpass
import time, os

class linkedin_crawler:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.browser_connection = None

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def input_username_password(self):
        self.set_username(input("Enter your username: "))
        self.set_password(getpass(prompt="Enter your password: ", stream=None))

    def set_browser_connection(self):
        PROJECT_ROOT = os.getcwd()
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
        self.browser_connection = webdriver.Chrome(executable_path=DRIVER_BIN)

    def get_browser_connection(self):
        return self.browser_connection

    def login(self):
        LOGIN_URL = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        browser = self.get_browser_connection()
        browser.get(LOGIN_URL)
        time.sleep(3)

        #Login
        elementID = browser.find_element_by_id('username')
        elementID.send_keys(self.username)
        elementID = browser.find_element_by_id('password')
        elementID.send_keys(self.password)
        elementID.submit()
        time.sleep(3)

    def get_profile_image_url(self, profile_page):
        page = soup(profile_page, features="html.parser")
        img = page.find("img", {"class": "pv-top-card__photo"})
        return img["src"]

    def search_profile(self, name):
        ID_URL = 'https://www.linkedin.com/in/'
        browser = self.get_browser_connection()
        browser.get(ID_URL+name)
        time.sleep(3)
        return browser.page_source

    def quit_browser(self):
        self.get_browser_connection().quit()