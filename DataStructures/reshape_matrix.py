from unittest import TestCase
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        new_mat = []
        for row in mat:
            for num in row:
                flatten.append(num)
                
        if r * c != len(flatten):   # when given parameters is NOT possible and legal
            return mat
        else:
            for row_index in range(r):
                new_mat.append(flatten[row_index * c : row_index * c + c])
            return new_mat


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        mat = [[1,2],[3,4]]
        r = 1
        c = 4
        result = self.solution.matrixReshape(mat, r, c)
        self.assertEqual(result, [[1,2,3,4]])
    
    def test_two(self):
        mat = [[1,2],[3,4]]
        r = 2
        c = 4
        result = self.solution.matrixReshape(mat, r, c)
        self.assertEqual(result, [[1,2],[3,4]])

