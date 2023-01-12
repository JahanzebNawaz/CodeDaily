from unittest import TestCase
from typing import List, Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rm = Counter(ransomNote)
        mg = Counter(magazine)

        for k, v in rm.items():
            if k not in mg or mg[k] < v:
                return False

        return True


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        ransomNote = "a"
        magazine = "b"
        result = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(result, False)
    
    def test_two(self):
        ransomNote = "aa"
        magazine = "aab"
        result = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(result, True)
    
