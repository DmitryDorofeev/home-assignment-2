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

    def has_text_field(self):
        wait = WebDriverWait(self.driver, 10)
        field = wait.until(
            EC.element_to_be_clickable((By.ID, 'id_text')))
        return field.is_displayed()

    def select_blog_by_id(self, num):
        select = self.driver.find_element_by_css_selector('#id_blog_chzn>.chzn-single')
        select.click()
        option = self.driver.find_element_by_css_selector('#id_blog_chzn .active-result:nth-child({})'.format(num))
        option.click()

    def go_to_topic_edit(self):
        self.driver.get('http://ftest.stud.tech-mail.ru/blog/topic/create/')

    def set_title(self, title):
        field = self.driver.find_element_by_id('id_title')
        field.send_keys(title)

    def set_short_text(self, text):
        field = self.driver.find_element_by_id('id_text_short')
        field.send_keys(text)

    def set_text(self, text):
        field = self.driver.find_element_by_id('id_text')
        field.send_keys(text)

    def get_content(self):
        content = self.driver.find_element_by_css_selector('.topic-content')
        return content.text

    def get_title(self):
        title = self.driver.find_element_by_css_selector('h1.topic-title>a')
        return title.text

    def save(self):
        form = self.driver.find_element_by_css_selector('.blogs-left>form')
        form.submit()

    def remove(self):
        remove_link = self.driver.find_element_by_css_selector('a.actions-delete')
        remove_link.click()
        remove_form = self.driver.find_element_by_css_selector('#content>form')
        remove_form.submit()

    def has_error(self):
        error = self.driver.find_element_by_class_name('system-message-error')
        return error.is_displayed()
