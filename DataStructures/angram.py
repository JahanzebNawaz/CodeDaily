from unittest import TestCase
from typing import List, Counter

class Solution:
    bool = False
    def Anagram(self, s,t):
        if len(s) != len(t):
            self.bool = False
            return False
        if len(s) == 0 and len(t) == 0:
            self.bool = True
            return True
        if s[0] in t:
            t.remove(s[0])
            s.remove(s[0])
            if len(s) == 0 and len(t) == 0:
                self.bool = True
                return True
            self.Anagram(s,t)
        else:
            self.bool = False
            return False

    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        self.Anagram(s,t)
        return self.bool


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        s = "anagram"
        t = "nagaram"
        result = self.solution.canConstruct(s, t)
        self.assertEqual(result, True)
    
    def test_two(self):
        s = "rat"
        t = "car"
        result = self.solution.canConstruct(s, t)
        self.assertEqual(result, False)
    
