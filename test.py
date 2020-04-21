import unittest
from pathlib import Path


class SudokuSolverTest(unittest.TestCase):
    def setUp(self):
        tests_folder = Path('./example/')

        self.example1 = (tests_folder / 'example1.txt').readlines()
        self.example2 = (tests_folder / 'example2.txt').readlines()
        self.example3 = (tests_folder / 'example3.txt').readlines()
        self.solved1 = (tests_folder / 'solved1.txt').readlines()
        self.solved2 = (tests_folder / 'solved2.txt').readlines()
        self.solved3 = (tests_folder / 'solved3.txt').readlines()


if __name__ == '__main__':
    unittest.main()
