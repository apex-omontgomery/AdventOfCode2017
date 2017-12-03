
import unittest
from solution import single_row, main_solution, max_min, even_divisor

class TestPart1(unittest.TestCase):
    def test_row_1(self):
        self.assertEqual(single_row('5 1 9 5', max_min), 8)

    def test_row_2(self):
        self.assertEqual(single_row('7 5 3', max_min), 4)

    def test_row_3(self):
        self.assertEqual(single_row('2 4 6 8', max_min), 6)

    def full_solution(self):
        self.assertEqual(main_solution(['5 1 9 5',
                                        '7 5 3',
                                        '2 4 6 8'],max_min), 18)

class TestPart2(unittest.TestCase):
    def test_row_1(self):
        self.assertEqual(single_row('5 9 2 8', even_divisor), 4)

    def test_row_2(self):
        self.assertEqual(single_row('9 4 7 3', even_divisor), 3)

    def test_row_3(self):
        self.assertEqual(single_row('3 8 6 5', even_divisor), 2)

    def full_solution(self):
        self.assertEqual(main_solution(['5 9 2 8',
                                       '9 4 7 3',
                                       '3 8 6 5'], even_divisor), 9)

