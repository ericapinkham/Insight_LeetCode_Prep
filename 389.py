import unittest

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    def letter_counts(string):
        d = {}
        for e in string:
            try:
                d[e] += 1
            except:
                d[e] = 1
        return d

    s_counts = letter_counts(s)
    t_counts = letter_counts(t)

    for t_key in t_counts.keys():
        if t_key not in s_counts or t_counts[t_key] != s_counts[t_key]:
            return t_key
    return ""

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(findTheDifference("abcde", "abcdef"), "f")
    def test2(self):
        self.assertEqual(findTheDifference("a", "aa"), "a")

if __name__ == '__main__':
    unittest.main()
