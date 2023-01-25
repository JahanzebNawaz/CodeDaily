
from unittest import TestCase
import textwrap


class Solution:
    def print_formatted(self, number):
        # your code goes here
        len_b = len(f'{number:b}')
        
        for i in range(1,number+1):
            print(f'{i:d}'.rjust(len_b), f'{i:o}'.rjust(len_b), f'{i:X}'.rjust(len_b), f'{i:b}'.rjust(len_b), end='\n') 



class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        result = self.solution.print_formatted(4)
    
