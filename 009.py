
import unittest

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    n = len(s)
    if len(s) == 1:
        return True
    l = s[:(n + 1) // 2:]
    r = s[n:n // 2 - 1:-1]
    print(l, r)
    return  l == r

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isPalindrome(121), True)
    def test2(self):
        self.assertEqual(isPalindrome(11), True)
    def test3(self):
        self.assertEqual(isPalindrome(12145), False)
    def test4(self):
        self.assertEqual(isPalindrome(0), True)

if __name__ == '__main__':
    unittest.main()
