import unittest
import sys
import os
# importing modules from analyzer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer.country_feature import print_patents


class TestMakeRequestCountry(unittest.TestCase):

    def test_valid_input(self):
        '''Testing valid inputs for print_patents,
        valid inputs:
        - string of a state name abbreviation for the parameter st,
        - n or p for the parameter val.'''

        self.assertEqual(print_patents('IT', 'n', False), 59700)
        self.assertEqual(print_patents('IT', 'p', False), 1)

    def test_wrong_input(self):
        '''Testing wrong-case inputs for print_patents,
        wrong inputs:
        - string of name different from a state abbreviation,
        - string different from n or p for the parameter val.'''

        # testing wrong st input
        self.assertEqual(print_patents('Mars', 'n', False), 0)

        # testing wrong val input
        self.assertEqual(print_patents('IT', 'l', False), 0)

    def test_corner_input(self):
        '''Testing corner-case inputs for print_patents,
        corner inputs:
        - empty string for the parameter st,
        - empty string for the parameter val.'''

        self.assertEqual(print_patents('', 'n', False), 0)
        self.assertEqual(print_patents('IT', '', False), 0)


if __name__ == '__main__':
    unittest.main()
