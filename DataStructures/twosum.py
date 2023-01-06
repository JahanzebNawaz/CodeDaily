from unittest import TestCase
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[y] == target - nums[x]:
                    return [x, y]


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        num_list = [2,7,11,15]
        result = self.solution.twoSum(nums=num_list, target=9)
        self.assertEqual(result, [0, 1])
    
    def test_two(self):
        num_list = [3,2,4]
        result = self.solution.twoSum(nums=num_list, target=6)
        self.assertEqual(result, [1, 2])
    
    def test_three(self):
        num_list = [3,3]
        result = self.solution.twoSum(nums=num_list, target=6)
        self.assertEqual(result, [0, 1])
