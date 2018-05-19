

import unittest

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set('aeiouAEIOU')
    l = 0
    r = len(s) - 1
    letters = [e for e in s]
    while l < r:
        while l < r and letters[l] not in vowels:
            l += 1
        while l < r and letters[r] not in vowels:
            r -= 1
        letters[l], letters[r] = letters[r], letters[l]
        l += 1
        r -= 1
    return "".join(letters)



class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverseVowels("hello"), "holle")
    def test2(self):
        self.assertEqual(reverseVowels("leetcode"), "leotcede")
    def test3(self):
        self.assertEqual(reverseVowels("sdsdsd"), "sdsdsd")
    def test4(self):
        self.assertEqual(reverseVowels(""), "")
    def test5(self):
        self.assertEqual(reverseVowels("aeiou"), "uoiea")
    def test6(self):
        self.assertEqual(reverseVowels("Aa"), "aA")


if __name__ == '__main__':
    unittest.main()
