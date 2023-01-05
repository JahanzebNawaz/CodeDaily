from unittest import TestCase
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        num_list = [-2,1,-3,4,-1,2,1,-5,4]
        result = self.solution.maxSubArray(nums=num_list)
        self.assertEqual(result, 6)
    
    def test_two(self):
        num_list = [1]
        result = self.solution.maxSubArray(nums=num_list)
        self.assertEqual(result, 1)
    
    def test_three(self):
        num_list = [5,4,-1,7,8]
        result = self.solution.maxSubArray(nums=num_list)
        self.assertEqual(result, 23)
