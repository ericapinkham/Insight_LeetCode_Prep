#!/usr/bin/python3
import random
import unittest

class min_int_heap():
    def __init__(self):
        self.items = [None] * 10
        self.capacity = 10
        self.size = 0

    def get_left_child_index(self, parent_index): return 2 * parent_index + 1
    def get_right_child_index(self, parent_index): return 2 * parent_index + 2
    def get_parent_index(self, index): return (index - 1) // 2

    def has_left_child(self, index): return self.get_left_child_index(index) < self.size
    def has_right_child(self, index): return self.get_right_child_index(index) < self.size
    def has_parent(self, index): return self.get_parent_index(index) >= 0

    def left_child(self, index): return self.items[self.get_left_child_index(index)]
    def right_child(self, index): return self.items[self.get_right_child_index(index)]
    def parent(self, index): return self.items[self.get_parent_index(index)]

    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def ensure_extra_capacity(self):
        if self.size == self.capacity:
            self.items.extend([None] * self.capacity)
            self.capacity *= 2

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.items[0]

    def poll(self):
        if self.size == 0:
            return None

        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()

        return item

    def add(self, item):
        self.ensure_extra_capacity()
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

class test(unittest.TestCase):
    def test1(self):
        nums = [random.randint(0, 10) for e in range(10)]
        h = min_int_heap()
        for n in nums:
            h.add(n)

        self.assertEqual(min(nums), h.poll())

if __name__ == '__main__':
    unittest.main()
