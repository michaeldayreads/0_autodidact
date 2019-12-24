# implemeation of, and reaction / response to:
# https://pymotw.com/3/unittest/index.html

import unittest

class ExampleZero(unittest.TestCase):

    def test_identity_success(self):
        value_at_0 = 'a'
        value_at_1 = 'a'
        self.assertEqual(value_at_0, value_at_1)
        
    def test_true(self):
        return

    # Not clear how to skip a test.
    # def test_false(self):
    #     self.assertTrue(False, "This is TDD: add implementation to make this true.")

    def test_raise_error(self):
        if True is False:
            raise RuntimeError("We should, of course, create specific errors.")


class ContainerTests(unittest.TestCase):

    def testDictExample(self):
        self.assertDictEqual(
            {'foo': 'bar', 'baz': 'qux'},
            {'baz': 'qux', 'foo': 'bar'},
        )

    def testDictExampleThatFails(self):
        self.assertDictEqual(
            {'foo': '8ar', 'baz': 'qux'},
            {'baz': 'qux', 'foo': 'bar'},
        )


class Membership(unittest.TestCase):

    def test_key_present(self):
        self.assertIn('foo', {'foo': 'bar', 'baz': 'qux'})

    def test_key_absent(self):
        self.assertIn('qux', {'foo': 'bar', 'baz': 'qux'}, "The term 'in' here is ambiguous.")