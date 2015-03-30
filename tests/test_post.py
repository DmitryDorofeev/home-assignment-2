__author__ = 'dmitry'

"""
Тесты добавления топиков, где топик не должен создаваться
"""

import unittest
from pages.page import PageObject

TITLE_BOUNDARY = 250
BOLD_LINE = '****'
ITALIC_LINE = '**'


class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.topic = PageObject()
        self.topic.login('ftest2@tech-mail.ru')
        self.topic.go_to_topic_edit()

    def tearDown(self):
        pass
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
        self.topic.set_title('text boundary test')
        self.topic.set_short_text('short_text')
        self.topic.bold()
        text = self.topic.get_editor_text()
        self.assertEqual(text, BOLD_LINE)

    def test_create_italic_text(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('text boundary test')
        self.topic.set_short_text('short_text')
        self.topic.italic()
        text = self.topic.get_editor_text()
        self.assertEqual(text, ITALIC_LINE)