
from unittest import TestCase
import re 


class Solution:

    def is_valid_credit_card(self, number):
        if not re.match(r'^[4-6]', number):
            return False
        if not re.match(r'^\d{16}$|^(\d{4}-){3}\d{4}$', number):
            return False
        if not re.match(r'^\d+$', number.replace("-", "")):
            return False
        if re.search(r'(\d)\1{3,}', number.replace("-", "")):
            return False
        return True

    def check(self, num, card_no):
        n = num
        credit_cards = []

        for i in range(n):
            credit_cards.append(card_no)

        for i in range(n):
            if self.is_valid_credit_card(credit_cards[i]):
                print("Valid")
            else:
                print("Invalid")


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_one(self):
        no_list = 1
        card_no = '4123456789123456'
        result = self.solution.check(no_list, card_no)
