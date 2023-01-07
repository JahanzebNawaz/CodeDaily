from unittest import TestCase
from typing import List

class Solution:
    def intersect(self, nums1, nums2):
        arr1 = sorted(nums1)
        arr2 = sorted(nums2)
        i,j = 0,0
        ans = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                ans.append(arr1[i])
                i += 1
                j += 1
        return ans


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        nums1 = [1,2,2,1]
        nums2 = [2,2]
        result = self.solution.intersect(nums1=nums1, nums2=nums2)
        self.assertEqual(result, [2, 2])
    
    def test_two(self):
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        result = self.solution.intersect(nums1=nums1, nums2=nums2)
        self.assertEqual(result, [4, 9])

