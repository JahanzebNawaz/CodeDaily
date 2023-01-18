
from unittest import TestCase


class Solution:
    def print_full_name(self, first, last):
        # Write your code here
        sentence = f"Hello {first} {last}! You just delved into python."
        return sentence

class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        first = "John"
        last = "Doe"
        result = self.solution.print_full_name(first, last)
        self.assertEqual(result, 'Hello John Doe! You just delved into python.')
