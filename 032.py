
#!/usr/bin/python3

import unittest

def longest_paren_substring(string):
    stack = [-1]
    max_len = 0
    for i, e in enumerate(string):
        if e == '(':
            stack.append(i)
        elif e == ')':
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                l = i - stack[-1]
                if l > max_len:
                    max_len = l
    return max_len


class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(longest_paren_substring("()()"), 4)
    def test2(self):
        self.assertEqual(longest_paren_substring("(()"), 2)
    def test3(self):
        self.assertEqual(longest_paren_substring(")()())"), 4)

if __name__ == '__main__':
    unittest.main()
