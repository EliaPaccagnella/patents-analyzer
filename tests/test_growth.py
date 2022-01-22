import unittest
import os
import sys
import io
from unittest.mock import patch

class Test_patents_country_years(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName=methodName)

    def setUp(self):
        print("\nStarting test...")
        return

    def tearDown(self):
        print("Test completed")
        return

    def test_valid_input(self):
        self.assertEqual(patents_country_years("IT", 1980, 1982), {'1980': 570, '1981': 672, '1982': 570})
        self.assertEqual(patents_country_years("US", 1999, 2003),{'1999': 77726, '2000': 80677, '2001': 83971, '2002': 82758,'2003': 84432})
        self.assertEqual(patents_country_years("JP", 1977, 1978),{'1977': 5839, '1978': 6558})

    def test_wrong_inputs(self):
        test_country = "UP"
        test_start = 1980
        test_end = 1985 
        response = "Sadly, we don't have data for {c} from {s} to {e}.\n".format(c=test_country, s=test_start, e=test_end)
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            patents_country_years(test_country, test_start, test_end)
        assert fake_stdout.getvalue() == response

        test_country = "CH"
        test_start = 1570
        test_end = 1577 
        response = "Sadly, we don't have data for {c} from {s} to {e}.\n".format(c=test_country, s=test_start, e=test_end)
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            patents_country_years(test_country, test_start, test_end)
        assert fake_stdout.getvalue() == response

if __name__=='__main__':
    unittest.main(verbosity=0)