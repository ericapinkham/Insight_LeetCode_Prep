import unittest

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    l = [None] * n

    for e in nums:
        if 0 < e < n + 1:
            l[e - 1] = e

    i = 1
    for e in l:
        if e is None:
            break
        i += 1
        print(e, i)

    return i

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(firstMissingPositive([1,2,3]), 4)
    def test2(self):
        self.assertEqual(firstMissingPositive([]), 1)
    def test3(self):
        self.assertEqual(firstMissingPositive([7,8,9]), 1)

if __name__ == '__main__':
    unittest.main()
