# -*- coding: utf-8 -*-
__author__ = 'dmitry'

"""
Тесты добавления топиков, где топик не должен создаваться
"""
import os
import unittest
from pages.page import PageObject

TITLE_BOUNDARY = 250
BOLD_LINE = '****'
ITALIC_LINE = '**'
QUOTE_LINE = '>'
UL_LINE = '* '
OL_LINE = '1. '
LINK_LINE = '[](http://mail.ru)'
IMG_URL = 'http://www.bmstu.ru/content/images/medium/img_2149.png'
IMG_LINE = '![]({})'.format(IMG_URL)
IMG_PATH = os.path.dirname(__file__) + '/images/pic.jpg'


class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.topic = PageObject()
        self.topic.login('ftest2@tech-mail.ru')
        self.topic.go_to_topic_edit()

    def tearDown(self):
        self.topic.close()

    def test_create_without_blog(self):
        self.topic.select_blog_by_id(1)
        self.topic.set_title('test')
        self.topic.set_short_text('test')
        self.topic.set_text('sample text')
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_without_title(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_short_text('test')
        self.topic.set_text('teeeext')
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_without_shorttext(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_text('sample text')
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_without_text(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('test')
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_title_long(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('x' * (TITLE_BOUNDARY + 1))
        self.topic.set_short_text('test')
        self.topic.set_text('sample text')
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_bold_text(self):
        self.topic.select_blog_by_id(2)
        self.topic.bold()
        text = self.topic.get_editor_short_text().strip()
        self.assertEqual(text, BOLD_LINE)

    def test_create_italic_text(self):
        self.topic.select_blog_by_id(2)
        self.topic.italic()
        text = self.topic.get_editor_short_text().strip()
        self.assertEqual(text, ITALIC_LINE)

    def test_create_quote(self):
        self.topic.select_blog_by_id(2)
        self.topic.quote()
        text = self.topic.get_editor_short_text().strip()
        self.assertEqual(text, QUOTE_LINE)

    def test_create_ul(self):
        self.topic.select_blog_by_id(2)
        self.topic.unordered_list()
        text = self.topic.get_editor_short_text()
        self.assertIn(UL_LINE, text)

    def test_create_ol(self):
        self.topic.select_blog_by_id(2)
        self.topic.ordered_list()
        text = self.topic.get_editor_short_text()
        self.assertIn(OL_LINE, text)

    def test_create_link(self):
        self.topic.select_blog_by_id(2)
        self.topic.link('http://mail.ru')
        text = self.topic.get_editor_short_text()
        self.assertIn(LINK_LINE, text)

    def test_insert_image(self):
        self.topic.select_blog_by_id(2)
        self.topic.insert_image(IMG_URL)
        text = self.topic.get_editor_short_text()
        self.assertIn(IMG_LINE, text)

    def test_upload_image(self):
        self.topic.select_blog_by_id(2)
        self.topic.load_image(IMG_PATH)
        text = self.topic.get_editor_short_text()
        self.assertIn('.jpg', text)