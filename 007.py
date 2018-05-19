
import unittest
from math import log10
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= 0:
        sign = 1
    else:
        sign = -1
    x = abs(x)
    r = 0
    if x > 0:
        i = int(log10(x))
    while x > 0:
        r, x = r + (x % 10) * 10 ** i, x // 10
        print(r, x)
        i -= 1

    return sign * r

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse(123), 321)
    def test2(self):
        self.assertEqual(reverse(-123), -321)
    def test3(self):
        self.assertEqual(reverse(0), 0)

if __name__ == '__main__':
    unittest.main()
