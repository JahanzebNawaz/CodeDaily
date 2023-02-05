
from unittest import TestCase
from datetime import datetime


class Solution:
    def timeConversion(self, time):
    # Write your code here
        dt = datetime.strptime(time, "%I:%M:%S%p")
        return dt.strftime("%H:%M:%S")
        


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        time = "07:05:45PM"
        result = self.solution.timeConversion(time=time)
        self.assertEqual(result,  "19:05:45")

    def test_one(self):
        time = "07:05:45AM"
        result = self.solution.timeConversion(time=time)
        self.assertEqual(result,  "07:05:45")