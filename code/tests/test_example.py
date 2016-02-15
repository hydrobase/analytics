import unittest

from code.example import is_even


class ExampleTest(unittest.TestCase):

    def test_odd_integer_returns_false(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(2.1))

    def test_even_integer_returns_true(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4.0))

    def test_raise_error_if_arg_not_number(self):
        with self.assertRaises(ValueError):
            is_even('one')
