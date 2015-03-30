__author__ = 'dmitry'

"""
Тесты добавления топиков, где топик должен создаваться
"""

import unittest
from pages.page import PageObject

TITLE_BOUNDARY = 250


class PostCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.topic = PageObject()
        self.topic.login('ftest2@tech-mail.ru')
        self.topic.go_to_topic_edit()

    def tearDown(self):
        pass
        self.topic.remove()
        self.topic.close()

    def test_create_ok(self):
        text = 'sampletext'
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('test')
        self.topic.set_text('sampletext')
        self.topic.save()
        self.assertEqual(self.topic.get_content(), text)

    def test_create_title_boundary(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('x' * TITLE_BOUNDARY)
        self.topic.set_short_text('test')
        self.topic.set_text('sample text')
        self.topic.save()
        self.assertEqual(self.topic.get_title(), 'x' * TITLE_BOUNDARY)