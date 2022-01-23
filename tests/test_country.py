import unittest
import sys
import os
# importing modules from analyzer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer.country_feature import print_patents


class TestMakeRequestCountry(unittest.TestCase):

    def test_valid_input(self):
        '''Testing valid inputs'''

        self.assertEqual(print_patents('IT', 'n'), 59700)
        self.assertEqual(print_patents('IT', 'p'), 1)

    def test_wrong_input(self):
        '''Testing wrong-case inputs'''

        # testing wrong st input
        self.assertEqual(print_patents('Mars', 'n'), 0)

        # testing wrong val input
        self.assertEqual(print_patents('IT', 'l'), 0)

    def test_corner_input(self):
        '''Testing corner-case inputs'''

        self.assertEqual(print_patents('', 'n'), 0)
        self.assertEqual(print_patents('IT', ''), 0)


if __name__ == '__main__':
    unittest.main()
