import unittest
from unittest.mock import patch
import lecture
from lecture import difficult_function, complex_math

class MyTestCase(unittest.TestCase):
    @patch("lecture.complex_math", return_value=0)
    def test_difficult_function0(self, mock_complex_math):
         self.assertEqual(first=difficult_function(0, 0), second="solved!")

    @patch("lecture.complex_math", return_value=1)
    def test_difficult_function1(self, mock_complex_math):
         self.assertEqual(first=difficult_function(1, 1), second="not yet")

    def test_complex_math0(self):
         self.assertEqual(first=complex_math(0, 0), second=15.137665311315716)

    def test_complex_math1(self):
         self.assertEqual(first=complex_math(0, 1), second=15.171841011518415)

    def test_complex_math2(self):
         self.assertEqual(first=complex_math(1, 1), second=14.442727523776187)
