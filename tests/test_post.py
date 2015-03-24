__author__ = 'dmitry'

import unittest
from pages.main_page import PageObject as MainPage


class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.page = MainPage()
        self.page.login('ftest2@tech-mail.ru')

    def tearDown(self):
        self.page.close()

    def test_open_edit(self):
        self.page.open_create_topic()