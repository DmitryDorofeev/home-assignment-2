__author__ = 'dmitry'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class PageObject():
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, os.environ.get('TTHA2BROWSER'))
        )
        self.driver.get('http://ftest.stud.tech-mail.ru/')

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
        wait = WebDriverWait(self.driver, 10)
        user = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'username')))
        return user.is_displayed()

    def close(self):
        self.driver.close()

    def open_create_topic(self):
        button = self.driver.find_element_by_id('modal_write_show')
        button.click()
        wait = WebDriverWait(self.driver, 10)
        button_write = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.write-item-type-topic>.write-item-link')))
        button_write.click()