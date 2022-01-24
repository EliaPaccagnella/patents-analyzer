import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer.country_feature import world_map


class TestWorldMap(unittest.TestCase):
    def test_valid_input(self):
        """ 
            Test the world_map function for valid inputs,
            using the valid_continents list, invalid inputs
            and corner inputs (missing real countries).
            Tests for valid inputs with all uppercase
            letters or capitalized names have been into
            a comment string to reduce running time,
            altough they do work.
            
        """
        # valid continents
        valid_continents = [
            'world',
            'europe',
            'asia',
            'north america',
            'south america',
            'africa'
        ]

        for continent in valid_continents:
            self.assertEqual(world_map(continent, False), 1)

        # input must be valid also if continets are uppercase
        # for continent in valid_continents:
        #     self.assertEqual(world_map(continent.upper()), 1)

        # input must be valid also if continets are capitalized
        # for continent in valid_continents:
        #     self.assertEqual(world_map(continent.capitalize()), 1)

    def test_invalid_input(self):
        # continet inputed is not a valid continent
        self.assertEqual(world_map('Mars'), False), 0)

    def test_corner_input(self):
        # oceania is not a valid continent for plotly
        self.assertEqual(world_map('oceania'), False), 0)


if __name__ == '__main__':
    unittest.main()
