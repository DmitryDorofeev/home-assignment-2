__author__ = 'dmitry'

import unittest
from pages.page import PageObject


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.page = PageObject()
        self.page.login('ftest2@tech-mail.ru')

    def tearDown(self):
        self.page.close()

    def test_open_edit(self):
        self.page.open_create_topic()
        self.assertTrue(self.page.has_text_field())