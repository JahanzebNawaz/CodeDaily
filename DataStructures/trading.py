from unittest import TestCase
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        nums = [7,1,5,3,6,4]
        result = self.solution.maxProfit(nums)
        self.assertEqual(result, 5)
    
    def test_two(self):
        nums = [7,6,4,3,1]
        result = self.solution.maxProfit(nums)
        self.assertEqual(result, 0)

