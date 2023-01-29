
from unittest import TestCase


class Solution:
    def minion_game(self, string):
        # your code goes here
        length = len(string)
        kevin_score, stuart_score = 0, 0
            
        for i in range(length):
            if string[i] in 'AEIOU': kevin_score += length - i
            else: stuart_score += length - i
                        
        if kevin_score > stuart_score: 
            print('Kevin', kevin_score)
            return f'Kevin {kevin_score}'
        elif kevin_score < stuart_score: 
            print('Stuart', stuart_score)
            return f'Stuart {stuart_score}'
        else: 
            print('Draw')
            return 'Draw'



class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        words = 'BANANA'
        result = self.solution.minion_game(words)
        self.assertEqual(result, 'Stuart 12')
