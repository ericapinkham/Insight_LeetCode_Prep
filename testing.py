
import unittest

def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
        else:
            return mid
    return l

def searchRange(nums, target):
    l = binary_search(nums, target - 0.5)
    r = binary_search(nums, target + 0.5)
    return [l,max(r - 1, len(nums) - 1)]

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(binary_search([1,2,3,4,4,5,5], 4.5), 5)
    def test2(self):
        self.assertEqual(binary_search([1,2,3,4,4,5,5], 5.5), 6)
    def test3(self):
        self.assertEqual(binary_search([1,2,3,4,4,5], 3.5), 3)
    def test4(self):
        self.assertEqual(binary_search([1,2,3,4,4,5,5], 4), 3)
    def test5(self):
        self.assertEqual(binary_search([1,2,3,4,4,5,5], 0.5), 0)
    def test6(self):
        self.assertEqual(binary_search([1,1,1,1,1], 0.5), 0)
    def test6(self):
        self.assertEqual(binary_search([1,1,1,1,1], 1.5), 4)
    def test7(self):
        self.assertEqual(binary_search([1,1,1,1,1], 1.5), 4)
    def test8(self):
        self.assertEqual(binary_search([1], 1.5), 0)
    def test9(self):
        self.assertEqual(binary_search([1], 0.5), 0)

    def test10(self):
        self.assertEqual(searchRange([1], 1), [0,0])
    def test9(self):
        self.assertEqual(searchRange([1,2,2,2,2], 2), [1,4])
    def test9(self):
        self.assertEqual(searchRange([1,2,2,2,3,5], 2), [1,3])
        searchRange
    # def test1(self):
    #     self.assertEqual(binary_search([1,2,3,4,4,5], 4.5), 5)


if __name__ == '__main__':
    unittest.main()
