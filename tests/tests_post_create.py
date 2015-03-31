# -*- coding: utf-8 -*-
__author__ = 'dmitry'

"""
Тесты добавления топиков, где топик должен создаваться
"""

import unittest
from pages.page import PageObject

TITLE_BOUNDARY = 250
TEST_TEXT = 'Test tetxt'
TEST_IMG = 'http://www.bmstu.ru/content/images/medium/img_2149.png'


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
        self.topic.set_text(text)
        self.topic.save()
        self.assertEqual(self.topic.get_content(), text)

    def test_create_title_boundary(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('x' * TITLE_BOUNDARY)
        self.topic.set_short_text('test')
        self.topic.set_text('sample text')
        self.topic.save()
        self.assertEqual(self.topic.get_title(), 'x' * TITLE_BOUNDARY)

    def test_create_with_poll(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('test')
        self.topic.set_text('text very long')
        question = 'Question'
        answer1 = 'answer No. 1'
        answer2 = 'answer 7'
        self.topic.add_poll(question, answer1, answer2)
        self.topic.save()
        ans1, ans2 = self.topic.find_poll()
        self.assertEqual(ans1, answer1)
        self.assertEqual(ans2, answer2)

    def test_create_bold(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('text')
        self.topic.set_text('**' + TEST_TEXT + '**')
        self.topic.save()
        text = self.topic.get_bold_text()
        self.assertEqual(text, TEST_TEXT)

    def test_create_italic(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('text')
        self.topic.set_text('*' + TEST_TEXT + '*')
        self.topic.save()
        text = self.topic.get_italic_text()
        self.assertEqual(text, TEST_TEXT)

    def test_create_ol(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('text')
        self.topic.set_text('1. ' + TEST_TEXT + '\n2. ')
        self.topic.save()
        text = self.topic.get_ol_text()
        self.assertEqual(text, TEST_TEXT)

    def test_create_ul(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('text')
        self.topic.set_text('* ' + TEST_TEXT + '\n* ')
        self.topic.save()
        text = self.topic.get_ul_text()
        self.assertEqual(text, TEST_TEXT)

    def test_create_with_img(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('text')
        self.topic.set_text('![]({})'.format(TEST_IMG))
        self.topic.save()
        src = self.topic.get_img_text()
        self.assertEqual(src, TEST_IMG)

    def test_create_with_user(self):
        self.topic.select_blog_by_id(2)
        self.topic.set_title('test')
        self.topic.set_short_text('text')
        self.topic.set_text('[Alkid](/profile/a.manilov/)')
        self.topic.save()
        href = self.topic.get_link()
        self.assertIn('/profile/a.manilov/', href)
