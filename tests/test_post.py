__author__ = 'dmitry'

import unittest
from pages.main_page import PageObject as MainPage


class PostTestCase(unittest.TestCase):
    def test_post_create(self):
        page = MainPage()
        page.login('ftest2@tech-mail.ru')
        page.close()