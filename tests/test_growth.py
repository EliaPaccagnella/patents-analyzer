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


if __name__=='__main__':
    unittest.main(verbosity=0)