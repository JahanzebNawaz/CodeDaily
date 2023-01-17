
from unittest import TestCase
from typing import List





class Solution:
    def swap_case(self, s):
        return s.swapcase()


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        words = 'HackerRank.com presents "Pythonist 2".'
        result = self.solution.swap_case(words)
        self.assertEqual(result, 'hACKERrANK.COM PRESENTS "pYTHONIST 2".')
