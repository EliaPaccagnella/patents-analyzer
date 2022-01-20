import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer import patentsview as api

class test_make_request(unittest.TestCase):

    def setUp(self):
        self.req = api.Request()
        print("Initializing test...")
        return

    def tearDown(self):
        del self.req
        print("Tests run")
        return

    def test_valid_input(self):
        # testing basic functioning of make request function
        self.req.make_request(query = '{"_and":[{"assignee_country":"IT"},{"patent_year":2020}]}',fields = ["patent_id"])
        self.assertEqual(self.req._Request__data,
                        json.loads('{"patents":[{"patent_id":"10524528"},{"patent_id":"10524914"},{"patent_id":"10525006"},{"patent_id":"10525072"},{"patent_id":"10525161"},{"patent_id":"10525429"},{"patent_id":"10525432"},{"patent_id":"10525653"},{"patent_id":"10525755"},{"patent_id":"10525948"},{"patent_id":"10525990"},{"patent_id":"10526053"},{"patent_id":"10526156"},{"patent_id":"10526365"},{"patent_id":"10526442"},{"patent_id":"10526735"},{"patent_id":"10526781"},{"patent_id":"10526794"},{"patent_id":"10526827"},{"patent_id":"10526892"},{"patent_id":"10526926"},{"patent_id":"10527052"},{"patent_id":"10527206"},{"patent_id":"10527209"},{"patent_id":"10527259"}],"count":25,"total_patent_count":2596}'))

    def test_wrong_input(self):
        # testing wrong endpoint error
        self.req.make_request(
            endpoint='wrong_endpoint',
            query='{"patent_number":"7861215"}'
        )
        # should raise a Endpoint Error, implement test for error

        # testing wrong query error
        self.req.make_request(
            query='{"patent_number:"7861215"}' # forgot closing "
        )
        # should raise a Syntax Error, implement test for error

        # testing wrong fields error
        self.req.make_request(
            query='{"patent_number":"7861215"}',
            fields=["patent_id","invntor_idd"] # inventor misspelling
            )
        # should raise a Syntax Error, implement test for error

    def test_corner_input(self):
        pass

class test_get_data(unittest.TestCase):

    def setUp(self):
        self.req = api.Request()
        print("Initializing test...")
        return
    
    def tearDown(self):
        del self.req
        print("Tests run")
        return

    def test_valid_input(self):
        self.req.make_request(
            query='{"patent_number":"7861215"}'
        )
        self.assertEqual(self.req.get_data(), self.req._Request__data)

    def test_wrong_input(self):
        pass

    def test_corner_input(self):
        pass


if __name__ == '__main__':
    unittest.main()
