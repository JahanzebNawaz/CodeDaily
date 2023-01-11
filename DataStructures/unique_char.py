from unittest import TestCase
from typing import List, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,j in(Counter(s).items()):
            if j == 1: return s.index(i)
        return -1


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        word = "leetcode"
        result = self.solution.firstUniqChar(s=word)
        self.assertEqual(result, 0)
    
    def test_two(self):
        word = "aabb"
        result = self.solution.firstUniqChar(s=word)
        self.assertEqual(result, -1)
    
