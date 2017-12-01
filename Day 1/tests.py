# check next item
# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

# check mid item
# 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
# 1221 produces 0, because every comparison is between a 1 and a 2.
# 123425 produces 4, because both 2s match each other, but no other digit has a match.
# 123123 produces 12.
# 12131415 produces 4.

import unittest
from solution import solution, solution_mid

class TestSimple(unittest.TestCase):
    def test_number_1122(self):
        self.assertEqual(solution('1122'), 3)

    def test_number_1111(self):
        self.assertEqual(solution('1111'), 4)

    def test_number_1234(self):
        self.assertEqual(solution('1234'), 0)

    def test_number_91212129( self):
        self.assertEqual(solution('91212129'), 9)

class TestMid(unittest.TestCase):
    def test_number_1212(self):
        self.assertEqual(solution_mid('1212'), 6)

    def test_number_1221(self):
        self.assertEqual(solution_mid('1221'), 0)

    def test_number_123425(self):
        self.assertEqual(solution_mid('123425'), 4)

    def test_number_123123( self):
        self.assertEqual(solution_mid('123123'), 12)

    def test_number_12131415( self):
        self.assertEqual(solution_mid('12131415'), 4)