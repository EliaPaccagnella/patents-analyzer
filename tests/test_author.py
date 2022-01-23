import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer.author_feature import print_patents


class TestMakeRequestAuthor(unittest.TestCase):

    def test_valid_input(self):
        ''' testing valid inputs for print_patents:
        valid inputs = name and surname must contains only letters,
        output must be either n or p'''

        self.assertEqual(print_patents('Scott', 'Davidson', 'n'), 1)
        self.assertEqual(print_patents('Scott', 'Davidson', 'p'), 1)

    def test_wrong_input(self):
        ''' testing wrong inputs for print_patents,
        - when name and surname contains numbers,
        - when output is not n or p'''

        # name and surname contains numbers
        self.assertEqual(print_patents('8', 'Davidson', 'n'), 0)
        self.assertEqual(print_patents('Scott', '7', 'n'), 0)
        self.assertEqual(print_patents('8', '7', 'n'), 0)
        # output different from n or p
        self.assertEqual(print_patents('Scott', 'Davidson', 'a'), 0)

    def test_corner_input(self):
        ''' testing corner inputs for print_patents,
        - when name and surname are not defined,
        - when output is not defined'''

        self.assertEqual(print_patents('Scott', '', 'n'), 0)
        self.assertEqual(print_patents('Scott', 'Davidson', ''), 0)
        self.assertEqual(print_patents('', 'Davidson', 'n'), 0)


if __name__ == '__main__':
    unittest.main()
