
from unittest import TestCase


class Solution:
    def solve(self, s):
        words = s.split()
        words = [x.capitalize() for x in words]
        word = ' '.join(words)
        return word


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        words = 'hacker rank'
        result = self.solution.solve(words)
        self.assertEqual(result, 'Hacker Rank')
