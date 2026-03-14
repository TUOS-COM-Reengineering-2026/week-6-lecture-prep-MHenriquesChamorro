import unittest
from lecture import is_palindrome

class MyTestCase(unittest.TestCase):
    def test_palindrome0(self):
        s = 'a'
        self.assertTrue(is_palindrome(s))

    def test_palindrome1(self):
        s = 'hello'
        self.assertFalse(is_palindrome(s))

    def test_palindrome2(self):
        s = 'madam'
        self.assertTrue(is_palindrome(s))

    def test_palindrome3(self):
        s = '0111111111111111110'
        self.assertTrue(is_palindrome(s))

    def test_palindrome4(self):
        s = ''
        self.assertTrue(is_palindrome(s))

    def test_palindrome_long(self):
       long_s = "".join(["1" for _ in range(2000)])
       self.assertTrue(is_palindrome(long_s))

    def test_palindrome5(self):
        s = 'aaba'
        self.assertFalse(is_palindrome(s))

    def test_palindrome6(self):
        s = 'aabaa'
        self.assertTrue(is_palindrome(s))

    def test_palindrome7(self):
        s = 'aabba'
        self.assertFalse(is_palindrome(s))