import requests
from unittest.mock import patch
import unittest
import translator

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'


class TestTranslate(unittest.TestCase):
    def SetUp(self):
        self.API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        self.API_KEY_false = '!trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

    def translate_me(self):
        translated_word = translator.translate_me('Hello', self.API_KEY)
        self.assertEqual(translated_word[0], 200)
        self.assertEqual(translated_word[1], 'Привет')
        translated_word = translator.translate_me('Hello', self.API_KEY_false)
        self.assertGreater(translated_word[0], 200)