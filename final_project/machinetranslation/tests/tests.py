''' EN-FR-EN translator unittest'''

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    ''' Translator test class '''

    def test_english_to_french(self):

        ''' tests English to French translation '''
        empty_str = ''
        self.assertEqual(english_to_french(empty_str),empty_str)
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_french_to_english(self):

        ''' tests French to English translation '''

        empty_str = ''
        self.assertEqual(french_to_english(empty_str),empty_str)
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()
