import unittest

"""
unittest のサンプルコード

* http://docs.python.jp/3/library/unittest.html
"""


def is_prime(n):
    """
    素数判定関数 (低パフォーマンス)
    """
    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, n - 1):
        if n % i == 0:
            return False

    return True


class PrimeTest(unittest.TestCase):

    def test_is_prime(self):
        """
        Test that number is prime or not.
        """
        data = [
            (0, False),
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
        ]

        for n, expect in data:
            with self.subTest(n=n, expect=expect):
                self.assertEqual(is_prime(n), expect)
