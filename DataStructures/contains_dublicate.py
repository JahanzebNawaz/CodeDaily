
from unittest import TestCase
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(list(set(nums))):
            return False 
        return True
    


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_dublicates(self):
        num_list = [1,2,3,1]
        result = self.solution.containsDuplicate(nums=num_list)
        self.assertTrue(result)
    
    def test_without_dublicates(self):
        num_list = [1,2,3]
        result = self.solution.containsDuplicate(nums=num_list)
        self.assertFalse(result)

