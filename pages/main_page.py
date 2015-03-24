__author__ = 'dmitry'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class PageObject():
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        self.driver.get("http://ftest.stud.tech-mail.ru/")

    def show_login_form(self):
        show_button = self.driver.find_element_by_css_selector('.login-button>a')
        show_button.click()

    def login(self, login):

        self.show_login_form()

        login_field = self.driver.find_element_by_css_selector('input[name=login]')
        password_field = self.driver.find_element_by_css_selector('input[name=password]')
        form = self.driver.find_element_by_id('popup-login-form')

        login_field.send_keys(login)
        password_field.send_keys(os.environ.get('TTHA2PASSWORD'))
        form.submit()

        self.driver.save_screenshot('screenie.png')

    def close(self):
        self.driver.close()