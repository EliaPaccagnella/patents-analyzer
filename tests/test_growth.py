import unittest
import os
import sys
import io
from unittest.mock import patch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer.growth import patents_country_years

'''
This file contains tests on the query "growth patents". Since this query shows 
the final output as a graph, we cannot do tests on the contents of the graphs.
However, we can step back and use inputs of the barchart (the dictionary) as 
our test analysis. So we verify the function "patents_country_years"
We test on cases where:
- inputs are correctly inserted
- inputs inserted are wrong or does not exist in API
- empty inputs
- some corner cases: inputs out of available range
'''

class Test_patents_country_years(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName=methodName)

    def setUp(self):
        print('\nStarting test...')
        return

    def tearDown(self):
        print('Test completed')
        return

    def test_valid_input(self):

        '''
        This tests valid inputs: 
        - the API must return some data for the given country 
        - Starting year > 1975
        - Ending year < 2022
        '''

        self.assertEqual(patents_country_years('IT', 1980, 1982), {'1980': 570, '1981': 672, '1982': 570})
        self.assertEqual(patents_country_years('US', 1999, 2003),{'1999': 77726, '2000': 80677, '2001': 83971, '2002': 82758,'2003': 84432})
        self.assertEqual(patents_country_years('JP', 1978, 1977),{'1977': 5839, '1978': 6558})

    def test_wrong_inputs(self):

        '''
        This tests wrong inputs. 
        CASE 1: the country does not exist
        CASE 2: the country is not in api
        CASE 3: the years inserted are out of range
        '''

        # CASE 1
        test_country = 'UP'
        test_start = 1980
        test_end = 1985 
        response = '\033[93mSadly, there is no data for country {c}.\033[37m'.format(c=test_country)
        self.assertEqual(
            patents_country_years(test_country, test_start, test_end),
            response)
        
        # CASE 2
        test_country = 'UK'
        test_start = 2009
        test_end = 2012 
        response = '\033[93mSadly, there is no data for country {c}.\033[37m'.format(c=test_country)
        self.assertEqual(
            patents_country_years(test_country, test_start, test_end),
            response)

        # CASE 3
        test_country = 'CH'
        test_start = 1570
        test_end = 1577 
        response = '\033[93mPlease make sure: starting year > 1975 and ending year < 2022.\033[37m'
        self.assertEqual(
            patents_country_years(test_country, test_start, test_end),
            response)

    def test_empty_string (self):

        '''
        This tests empty inputs. 
        CASE 1: the country is empty
        CASE 2: the year is empty
        '''

        # CASE 1
        test_country = ''
        test_start = 1977
        test_end = 1978
        response = '\033[93mSadly, there is no data for country {c}.\033[37m'.format(c=test_country)
        self.assertEqual(patents_country_years(test_country, test_start, test_end), response)
        
    def corner_case (self):

        '''
        This tests some corner cases inputs. 
        CASE 1: when test_start is out of range
        CASE 2: when test_end is out of range
        CASE 3: when start > end and are out of range
        '''

        # CASE 1
        test_country = 'DE'
        test_start = 1700
        test_end = 1980
        response = '\033[93mPlease make sure: starting year > 1975 and ending year < 2022.\033[37m'
        self.assertEqual(patents_country_years(test_country, test_start, test_end), response)

        # CASE 2
        test_country = 'DE'
        test_start = 2020
        test_end = 2024
        response = '\033[93mPlease make sure: starting year > 1975 and ending year < 2022.\033[37m'
        self.assertEqual(patents_country_years(test_country, test_start, test_end), response)
    
if __name__=='__main__':
    unittest.main(verbosity=0)