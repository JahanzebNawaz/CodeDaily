
from unittest import TestCase


class Solution:
    def merge_the_tools(self, string, k):
    # your code goes here
        if k == 1:
            for x in string:
                print(x)
            return
        else:
            lis = []
            for i in range(k):
                x = string[k * i: k * i + k]
                lis.append(x)
            for i in lis:
                s = ''
                for word in i:
                    if word not in s:
                        s+=word
                    else:
                        continue
                print(s)


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        words = 'AABCAAADA'
        no = 3
        result = self.solution.merge_the_tools(words, no)
