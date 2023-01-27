
from unittest import TestCase


class Solution:
    def print_rangoli(self, size):
        # your code goes here
        height = 2*size - 1
        width = 2*height - 1

        l = []
        next_mid = chr(96 + size)

        for i in range(size, -size+1, -1):
            if i == size:
                # first character
                l.append(next_mid)
            elif i in range(size, 0, -1):
                # top and middle
                middle = len(l)//2
                previous_mid = next_mid
                next_mid = chr(96 + i)
                l.insert(middle, next_mid)
                l.insert(middle, previous_mid)
            else:
                # bottom
                middle = len(l)//2
                l.pop(middle)
                l.pop(middle)
            string = '-'.join(l)
            string = string.center(width, '-')
            print(string)


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        self.solution.print_rangoli(5)
