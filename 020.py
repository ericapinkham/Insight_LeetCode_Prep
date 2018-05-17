
import unittest

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    matching = {'{': '}', '(': ')', '[': ']'}
    for e in s:
        if e in ['[', '{', '(']:
            stack.append(e)
        else:
            if stack and e == matching[stack[-1]]:
                stack.pop()
            else:
                return False
    return not stack


class test(unittest.TestCase):

    def test1(self):
        self.assertEqual(isValid("{}{}[]{}"), True)

    def test2(self):
        self.assertEqual(isValid("()(()((([][]{[]}))))"), True)

    def test3(self):
        self.assertEqual(isValid("())"), False)

if __name__ == '__main__':
    unittest.main()
