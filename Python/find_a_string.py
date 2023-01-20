
from unittest import TestCase


class Solution:
    
    def count_substring(self, string: str, sub_string: str) -> int:
        count = 0
        for i in range(len(string)):
            current_string = string[i:i + len(sub_string)]
            if current_string == sub_string:
                count += 1
        return count


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        string = "ABCDCDC"
        sub_string = "CDC"
        result = self.solution.count_substring(string, sub_string)
        self.assertEqual(result, 2)
