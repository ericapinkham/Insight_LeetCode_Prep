import unittest

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        search_index = l + (r - l) // 2
        search_num = nums[search_index]
        if target == search_num:
            return search_index
        elif target > search_num:
            l = search_index + 1
        else:
            r = search_index - 1
    return l

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(searchInsert([1,3,5,6], 5), 2)
    def test2(self):
        self.assertEqual(searchInsert([1,3,5,6], 2), 1)
    def test3(self):
        self.assertEqual(searchInsert([1,3,5,6], 7), 4)
    def test4(self):
        self.assertEqual(searchInsert([1,3,5,6], 0), 0)


if __name__ == '__main__':
    unittest.main()
