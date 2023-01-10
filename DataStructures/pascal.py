from unittest import TestCase
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        if numRows == 1:
            return answer
        else:
            for i in range(2,numRows+1):
                row_prev = answer[i-2]
                row_curr = [1]
                for n in range(len(row_prev)-1):
                    row_curr.append(row_prev[n] + row_prev[n+1])
                row_curr.append(1)
                answer.append(row_curr)
            return answer


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        num = 5
        result = self.solution.generate(numRows=num)
        self.assertEqual(result, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
    
    def test_two(self):
        num = 1
        result = self.solution.generate(numRows=num)
        self.assertEqual(result, [[1]])
    
