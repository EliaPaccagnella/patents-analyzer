import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer.country_feature import world_map


class TestWorldMap(unittest.TestCase):
    def test_valid_input(self):
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
            self.assertEqual(world_map(continent), 1)

        # input must be valid also if continets are uppercase
        for continent in valid_continents:
            self.assertEqual(world_map(continent.upper()), 1)

        # input must be valid also if continets are capitalized
        for continent in valid_continents:
            self.assertEqual(world_map(continent.capitalize()), 1)

    def test_invalid_input(self):
        # continet inputed is not a valid continent
        self.assertEqual(world_map('Mars', 0))

    def test_corner_input(self):
        # oceania is not a valid continent for plotly
        self.assertEqual(world_map('oceania'), 0)


if __name__ == '__main__':
    unittest.main()
