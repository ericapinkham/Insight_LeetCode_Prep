
import unittest

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1

    l = [None] * (len(nums) + 1)
    for key, val in d.items():
        if l[val]:
            l[val].append(key)
        else:
            l[val] = [key]

    print(l)
    out = []
    i = len(nums)
    while len(out) < k:
        if l[i]:
            out.append(l[i])
        else:
            i -= 1

    return out


class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(topKFrequent([1,1,1,2,2,3], 2), [1,2])
    def test2(self):
        self.assertEqual(topKFrequent([1,2,3], 3), [1,2,3])
    def test3(self):
        self.assertEqual(topKFrequent([1,1,2,2,3], 1), [1])
    def test4(self):
        self.assertEqual(topKFrequent([1,1,1], 1), [1])

if __name__ == '__main__':
    unittest.main()
