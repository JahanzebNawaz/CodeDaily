
from unittest import TestCase
from typing import List

class Solution:
    def hash_tuple(self, tuple_data: tuple) -> List[str]:
        return hash(tuple_data)


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        tuple_data = (1, 2)
        result = self.solution.hash_tuple(tuple_data=tuple_data)
        self.assertEqual(result, -3550055125485641917)
