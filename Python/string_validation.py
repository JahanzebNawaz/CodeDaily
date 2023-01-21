
from unittest import TestCase


class Solution:
    
    def string_validate(self, string) :
        mylist = [False, False, False, False, False]
        for a in string:
            if a.isalnum() == True:
                mylist[0] = True
            if a.isalpha() == True:
                mylist[1] = True
            if a.isdigit() == True:
                mylist[2] = True
            if a.islower() == True:
                mylist[3] = True
            if a.isupper() == True:
                mylist[4] = True

        return mylist


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        string = "qA2"
        result = self.solution.string_validate(string)
        self.assertEqual(result, [True, True, True, True, True])
