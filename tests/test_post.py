__author__ = 'dmitry'

import unittest
from pages.page import PageObject


class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.page = PageObject()
        self.page.login('ftest2@tech-mail.ru')

    def tearDown(self):
        self.page.close()

    def test_create_ok(self):
        text = 'sampletext'
        self.page.go_to_topic_edit()
        self.page.select_blog_by_id(2)
        self.page.set_title('test')
        self.page.set_short_text('test')
        self.page.set_text('sampletext')
        self.page.save()
        self.assertEqual(self.page.get_content(), text)
        self.page.remove_topic()

    def test_create_without_blog(self):
        self.page.go_to_topic_edit()
        self.page.select_blog_by_id(1)
        self.page.set_title('test')
        self.page.set_short_text('test')
        self.page.set_text('azaza')
        self.page.save()
        self.assertTrue(self.page.has_error())

    def test_create_without_title(self):
        self.page.go_to_topic_edit()
        self.page.select_blog_by_id(2)
        self.page.set_short_text('test')
        self.page.set_text('azaza')
        self.page.save()
        self.assertTrue(self.page.has_error())