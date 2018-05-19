

import unittest




def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    out = []
    m = len([e for e in S if e.isalpha()])
    for i in range(2 ** m):
        new_str = ''
        j = 0
        for e in S:
            if e.isalpha():
                if 2 ** j & i:
                    new_str += e.upper()
                else:
                    new_str += e.lower()
                j += 1
            else:
                new_str += e

        out.append(new_str)
    return out


class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(letterCasePermutation("a23"), ["a23", "A23"])
    def test2(self):
        self.assertEqual(letterCasePermutation("123"), ["123"])
    def test3(self):
        self.assertEqual(letterCasePermutation("a2c"), ["a2c", "A2c", "a2C", "A2C"])
    def test4(self):
        self.assertEqual(letterCasePermutation("mQe"), ["mqe","mqE","mQe","mQE","Mqe","MqE","MQe","MQE"])

if __name__ == '__main__':
    unittest.main()
