import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.converter import MorseCodeConverter

class TestMorseCodeConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = MorseCodeConverter()
    
    def test_text_to_morse_basic(self):
        result = self.converter.text_to_morse('SOS')
        self.assertEqual(result['morse'], '... --- ...')
        self.assertIsNone(result['error'])
    
    def test_text_to_morse_with_spaces(self):
        result = self.converter.text_to_morse('HELLO WORLD')
        self.assertEqual(result['morse'], '.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
    
    def test_text_to_morse_lowercase(self):
        result = self.converter.text_to_morse('hello')
        self.assertEqual(result['morse'], '.... . .-.. .-.. ---')
    
    def test_text_to_morse_numbers(self):
        result = self.converter.text_to_morse('123')
        self.assertEqual(result['morse'], '.---- ..--- ...--')
    
    def test_morse_to_text_basic(self):
        result = self.converter.morse_to_text('... --- ...')
        self.assertEqual(result['text'], 'SOS')
        self.assertIsNone(result['error'])
    
    def test_morse_to_text_with_spaces(self):
        result = self.converter.morse_to_text('.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
        self.assertEqual(result['text'], 'HELLO WORLD')
    
    def test_bidirectional_conversion(self):
        original = 'PYTHON'
        morse_result = self.converter.text_to_morse(original)
        text_result = self.converter.morse_to_text(morse_result['morse'])
        self.assertEqual(text_result['text'], original)
    
    def test_unknown_characters(self):
        result = self.converter.text_to_morse('Hello#')
        self.assertIn('?', result['morse'])
    
    def test_empty_input_text_to_morse(self):
        result = self.converter.text_to_morse('')
        self.assertIsNotNone(result['error'])
    
    def test_empty_input_morse_to_text(self):
        result = self.converter.morse_to_text('')
        self.assertIsNotNone(result['error'])
    
    def test_validate_morse_input_valid(self):
        self.assertTrue(self.converter.validate_morse_input('... --- ...'))
    
    def test_validate_morse_input_invalid(self):
        self.assertFalse(self.converter.validate_morse_input('abc'))
    
    def test_get_supported_characters(self):
        chars = self.converter.get_supported_characters()
        self.assertIn('A', chars)
        self.assertIn('0', chars)
        self.assertNotIn(' ', chars)  #shouldn't be in supported list

if __name__ == '__main__':
    unittest.main()