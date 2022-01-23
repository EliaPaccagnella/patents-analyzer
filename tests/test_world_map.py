import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(_file_))))
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
            self.assertEqual(world_map(continent),1)
        
        # input must be valid also if continets are uppercase
        for continent in valid_continents:
            self.assertEqual(world_map(continent.upper()),1)
        
        # input must be valid also if continets are capitalized
        for continent in valid_continents:
            self.assertEqual(world_map(continent.capitalize()),1)
    
    def test_invalid_input(self):
        # continet inputed is not a valid continent
        self.assertEqual(world_map('Mars',0))
    




if _name_ == '_main_':
    unittest.main()