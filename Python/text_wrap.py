
from unittest import TestCase
import textwrap


class Solution:

    def wrap(self, string, max_width):
        # wrod wrap, textwrap package helps us to wrap the sentence
        a = textwrap.fill(string, max_width)
        return a


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        text = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
        result = self.solution.wrap(text, 4)
        print(result)
    
