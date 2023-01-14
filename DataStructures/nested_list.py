
from unittest import TestCase
from typing import List

class Solution:
    def nested_list(self, students: List[list]) -> List[str]:
        # hanckerRank input 
        # for _ in range(int(input())):
        #     name = input()
        #     score = float(input())
        #     records.append([name, score])

        records = students if students else []
        records.sort(key=lambda x: x[1])
        second_lowest_grade = sorted(set([student[1] for student in records]))[1]

        students = []

        for std in records:
            if std[1] == second_lowest_grade:
                students.append(std)

        students.sort(key=lambda x: x[0])

        return [x[0] for x in students]



class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
        result = self.solution.nested_list(students=students)
        self.assertEqual(result, ['Berry', 'Harry'])
