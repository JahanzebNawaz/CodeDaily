
from unittest import TestCase
from itertools import product



class Solution:

    def check_itertool(self):
        list1 = list(map(int, input().split()))
        list2 = list(map(int, input().split()))

        print(*list(product(list1, list2)))



class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        result = self.solution.check_itertool()
