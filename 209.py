import unittest

def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    min_l = 0
    left = len(nums) - 1
    sum = 0
    while nums and (left >= 0 or sum >= s):

        if sum < s:
            sum += nums[left]
            l += 1
            left -= 1

        if sum >= s:
            if min_l > l or min_l == 0:
                min_l = l
            sum -= nums.pop()
            l -= 1

    if sum >= s and (min_l > l or min_l == 0):
        min_l = l

    return min_l

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(minSubArrayLen(7, [2,3,1,2,4,3]), 2)
    def test2(self):
        self.assertEqual(minSubArrayLen(19, [2,3,1,2,4,3]), 0)
    def test3(self):
        self.assertEqual(minSubArrayLen(5, [1,1,1,1,1]), 5)
    def test4(self):
        self.assertEqual(minSubArrayLen(3, [1,2,1,1,1]), 2)
    def test5(self):
        self.assertEqual(minSubArrayLen(4, [4,0,1,1,1]), 1)
    def test6(self):
        self.assertEqual(minSubArrayLen(11, [1,2,3,4,5]), 3)

if __name__ == '__main__':
    unittest.main()
