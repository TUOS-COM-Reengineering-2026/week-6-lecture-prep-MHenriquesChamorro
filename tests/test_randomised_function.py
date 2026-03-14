import unittest
from unittest.mock import patch
from lecture import randomised_function

class MyTestCase(unittest.TestCase):
    @patch("random.randint", return_value=1)
    def test_small_radnint(self, mock_randint):
        self.assertEqual('software', randomised_function())
    
    @patch("random.randint", return_value=9)
    def test_large_radnint(self, mock_randint):
        self.assertEqual('engineering', randomised_function())