
from unittest import TestCase


class Solution:
    def solve(self, s):
        temp = s.split()
        for word in temp:
            s = s.replace(word, word.capitalize())
        return s


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        words = 'hacker rank'
        result = self.solution.solve(words)
        self.assertEqual(result, 'Hacker Rank')
