import unittest
from un_math import multiply

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12, 'Multiplication works')

    def test_strings(self):
        self.assertEqual(multiply('a', 3), 'aaa', 'Letters too')

    def test_none(self):
        self.assertEqual(multiply(None, None), None, 'Did this work?')


if __name__ == '__main__':
    unittest.main()
