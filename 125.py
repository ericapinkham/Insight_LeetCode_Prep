#!/usr/bin/python3

import unittest

def is_palindrome(string):
    if not string:
        return false
    s = "".join([e.lower() for e in string if e.isalnum()])
    n = len(s)
    return s[:n // 2:] == s[n:n // 2:-1]

class test(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_palindrome("dogod"), True)

    def test2(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal: Panama"), True)

    def test3(self):
        self.assertEqual(is_palindrome("asdasdasd"), False)

    def test4(self):
        self.assertEqual(is_palindrome("a"), True)

    def test5(self):
        self.assertEqual(is_palindrome("aa"), True)
if __name__ == '__main__':
    unittest.main()
