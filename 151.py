#!/usr/bin/python3
import unittest

def reverse_words(string):
    return " ".join([w for w in string.split()][::-1])

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_words("gus is a good dog"), "dog good a is gus")
    def test2(self):
        self.assertEqual(reverse_words("the sky is blue"), "blue is sky the")
    def test3(self):
        self.assertEqual(reverse_words("multiple     spaces"), "spaces multiple")
    def test4(self):
        self.assertEqual(reverse_words("       leading spaces     "), "spaces leading")

if __name__ == '__main__':
    unittest.main()
