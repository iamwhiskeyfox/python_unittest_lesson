from unittest import TestCase
from functions.email_regex import is_correct_email

class EmailRegexTestCase(TestCase):
    def test_is_correct_email(self):
        self.assertTrue(is_correct_email('themonrealstudio@gmail.com'))
        self.assertTrue(is_correct_email('masteraalish@gmail.com'))

    def test_is_correct_email_contains_two_add_symbols(self):
        self.assertFalse(is_correct_email('themonrea@lstudio@gmail.com'))

    def test_is_correct_email_does_not_contains_username(self):
        self.assertFalse(is_correct_email("@gmail.com"))

    def test_is_correct_email_does_not_contains_ad_symbol(self):
        self.assertFalse(is_correct_email('aidana.yahoo.com'))