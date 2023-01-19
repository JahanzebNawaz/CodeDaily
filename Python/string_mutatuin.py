
from unittest import TestCase


class Solution:
    def mutate_string(self, string, position, character):
        words_list = list(string)
        words_list[position] = character
        words = ''.join(words_list)
        return words

class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        string = "abracadabra"
        position = 5
        character = 'k'
        result = self.solution.mutate_string(string, position, character)
        self.assertEqual(result, "abrackdabra")
