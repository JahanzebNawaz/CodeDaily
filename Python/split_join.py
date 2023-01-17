
from unittest import TestCase


class Solution:
    def split_and_join(self, line):
        # write your code here
        line_list = line.split(" ")
        result = "-".join(line_list)
        return result


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        words = 'HackerRank.com presents Pythonist 2'
        result = self.solution.split_and_join(words)
        self.assertEqual(result, 'HackerRank.com-presents-Pythonist-2')
