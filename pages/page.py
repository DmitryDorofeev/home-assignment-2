__author__ = 'dmitry'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import os


SHORT_TEXT_FIELD = '(//*[@class="CodeMirror-scroll"])[1]'
TEXT_FIELD = '(//*[@class="CodeMirror-scroll"])[2]'


class PageObject():
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:5555/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, os.environ.get('TTHA2BROWSER', 'CHROME'))
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
        self.driver.quit()

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
            EC.visibility_of_element_located((By.XPATH, TEXT_FIELD)))
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
        field = self.driver.find_element_by_xpath(SHORT_TEXT_FIELD)
        field.click()
        ActionChains(self.driver).send_keys(text).perform()

    def set_text(self, text):
        field = self.driver.find_element_by_xpath(TEXT_FIELD)
        field.click()
        ActionChains(self.driver).send_keys(text).perform()

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

    def bold(self):
        bold_btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-bold')
        bold_btn.click()

    def italic(self):
        italic_btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-italic')
        italic_btn.click()

    def quote(self):
        quote_btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-quote')
        quote_btn.click()

    def unordered_list(self):
        ul_btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-unordered-list')
        ul_btn.click()

    def ordered_list(self):
        ol_btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-ordered-list')
        ol_btn.click()

    def link(self, link):
        link_btn = self.driver.find_element_by_xpath('//*[@id="container"]//a[@class="markdown-editor-icon-link"][1]')
        link_btn.click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()

    def insert_image(self, link):
        img_btn = self.driver.find_element_by_xpath('//*[@id="container"]//a[@class="markdown-editor-icon-image"][1]')
        img_btn.click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()

    def load_image(self, path):
        self.driver.find_element_by_xpath('(//input[@name="filedata"])[1]').send_keys(path)
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, '(//input[@name="filedata"])[1]')))
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda _: self.driver.find_element_by_xpath(SHORT_TEXT_FIELD).text.strip() != ''
        )


    def insert_user(self):
        quote_btn = self.driver.find_element_by_xpath('//*[@id="container"]//a[@class="markdown-editor-icon-link"][2]')
        quote_btn.click()

    def ordered_list(self):
        quote_btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-ordered-list')
        quote_btn.click()

    def preview(self):
        quote_btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-preview')
        quote_btn.click()

    def add_poll(self, question, answer1, answer2):
        poll_checkbox = self.driver.find_element_by_css_selector('#container [name="add_poll"]')
        poll_checkbox.click()
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_question"]')))
        elem.send_keys(question)
        ans1 = self.driver.find_element_by_id('id_form-0-answer')
        ans2 = self.driver.find_element_by_id('id_form-1-answer')
        ans1.send_keys(answer1)
        ans2.send_keys(answer2)

    def select_text(self):
        field = self.driver.find_element_by_id('id_text')
        field.click()
        self.driver.implicitly_wait(10)

    def get_editor_short_text(self):
        wait = WebDriverWait(self.driver, 10)
        field = wait.until(
            EC.element_to_be_clickable((By.XPATH, SHORT_TEXT_FIELD)))
        return field.text

    def get_editor_text(self):
        wait = WebDriverWait(self.driver, 10)
        field = wait.until(
            EC.element_to_be_clickable((By.XPATH, TEXT_FIELD)))
        return field.text

    def find_poll(self):
        ans1 = self.driver.find_element_by_xpath('.//ul[@class="poll-vote"]/li[1]/label').text
        ans2 = self.driver.find_element_by_xpath('.//ul[@class="poll-vote"]/li[2]/label').text
        return ans1, ans2

    def get_bold_text(self):
        try:
            text = self.driver.find_element_by_xpath('//*[contains(@class,"topic-content")]/p/strong').text
        except NoSuchElementException:
            return None
        return text

    def get_italic_text(self):
        try:
            text = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]/p/em').text
        except NoSuchElementException:
            return None
        return text

    def get_ol_text(self):
        try:
            text = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]/ol').text
        except NoSuchElementException:
            return None
        return text

    def get_ul_text(self):
        try:
            text = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]/ul').text
        except NoSuchElementException:
            return None
        return text

    def get_img_text(self):
        try:
            url = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]/p/img').get_attribute('src')
        except NoSuchElementException:
            return None
        return url

    def get_link(self):
        try:
            link = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]/p/a').get_attribute('href')
        except NoSuchElementException:
            return None
        return link