
from unittest import TestCase
from typing import List

class Solution:
    def get_data(self) -> List[str]:
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        student = student_marks[query_name]
        result = sum(student)/ len(student)
        avg_result = f"{result:.2f}"
        return avg_result


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        # could use different way to assert Check
        result = self.solution.get_data()
        self.assertIsNotNone(result)
