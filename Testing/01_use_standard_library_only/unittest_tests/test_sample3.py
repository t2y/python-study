import unittest
from datetime import datetime
from unittest.mock import patch

"""
unittest.mock のサンプルコード

* http://docs.python.jp/3/library/unittest.mock.html
"""

def greet(name):
    now = datetime.now()
    if now.hour < 12:
        return '%s, good morning' % name
    elif 12 <= now.hour < 16:
        return '%s, good afternoon' % name
    else:
        return '%s, good evening' % name


class Greeting:

    def __init__(self, name):
        self.name = name

    def do_greet(self):
        return greet(self.name)


class GreetingTestCase(unittest.TestCase):

    @patch('unittest_tests.test_sample3.greet')
    def test_greet(self, mock_greet):
        name = 'john'
        expected = '%s, good night' % name

        mock_greet.return_value = expected
        actual = greet(name)
        self.assertEqual(actual, expected)

        # assert greet function is called with this parameter
        mock_greet.assert_called_with(name)

    @patch.object(Greeting, 'do_greet')
    def test_obj_greet(self, mock_obj_greet):
        name = 'bob'
        expected = '%s, hello' % name

        mock_obj_greet.return_value = expected
        g = Greeting(name)
        actual = g.do_greet()
        self.assertEqual(actual, expected)

        # assert Greeting.greet method is called with these parameter
        mock_obj_greet.assert_called_with()
