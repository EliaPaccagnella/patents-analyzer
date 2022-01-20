from dataclasses import fields
import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer import patentsview as api
from analyzer.errors import errors

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

        # testing invalid query syntax
        with self.assertRaises(errors.SyntaxError):
            self.req.make_request(
               query=('{"_and:[{"assignee_country":"IT"},' # missing closing "
                      '{"patent_year":2020}]}')
            )

        with self.assertRaises(errors.SyntaxError):
            self.req.make_request(
               query='{"patent_nuber":"7861215"}' # misspelling number
            )

        # testing invalid field syntax
        with self.assertRaises(errors.SyntaxError):
            self.req.make_request(
               query=('{"_and:"[{"assignee_country":"IT"},'
                      '{"patent_year":2020}]}'),
               fields=["patnt_id"] # misspelling patent
            )
        # syntax errors in fields are handled automatically by Python
        with self.assertRaises(SyntaxError):
            eval("""self.req.make_request(
                query='{"patent_number":"7861215"}',
                fields=['patent_id','inventor_id]
            )""")

        # testing request without query
        with self.assertRaises(errors.MissingQuery):
            self.req.make_request()

        # testing invalid endpoint
        with self.assertRaises(errors.InvalidEndpoint):
            self.req.make_request(
                endpoint='wrong_endpoint',
                query='{"patent_number":"7861215"}'
            )

        # testing for custom errors raising
        # source: https://bit.ly/3JwcDOp

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
        # testing data request before using the make_request method
        with self.assertRaises(errors.NoData):
            self.req.get_data()

    def test_corner_input(self):
        # testing the case in which the make_request method returns no data
        self.req.make_request(
            query=('{"_and":[{"assignee_country":"IT"},'
                   '{"patent_year":2022}]}'),
            fields=["patent_id"]
        )
        self.assertEqual(self.req.get_data(), self.req._Request__data)


if __name__ == '__main__':
    unittest.main()
