import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.testcase):

    def setUp(self):
        pass


    def test_non_marked_lines(self):
        '''Only <p> tags'''
        self.assertEqual('this line has no special handling', actual, 'message')
