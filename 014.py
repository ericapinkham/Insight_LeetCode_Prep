#!/usr/bin/python3

import unittest
from functools import reduce

def longest_common_prefix(words):
    def longest_prefix_2(left, right):
        pre = ""
        for (e, f) in zip(left, right):
            if e == f:
                pre += e
            else:
                break
        return pre

    if not words:
        return ""
    elif len(words) == 1:
        return words[0]

    return reduce(longest_prefix_2, words)


class test(unittest.TestCase):

    def test1(self):
        self.assertEqual(longest_common_prefix(["dog", "cat"]), "")

    def test2(self):
        self.assertEqual(longest_common_prefix(["dog", "dog"]), "dog")

    def test3(self):
        self.assertEqual(longest_common_prefix(["gus", "gussy", "gud"]), "gu")

if __name__ == '__main__':
    unittest.main()
