import unittest
import json
import sys
import os
from unittest.mock import patch
import io
# importing modules from analyzer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer import patentsview as api
from analyzer.errors import errors


class TestMakeRequestCountry(unittest.TestCase):

    def setUp(self):
        '''Before every test this method creates a new Request object'''
        self.req = api.Request()
        print("\nInitializing test varibles...")
        return

    def tearDown(self):
        '''After every test, this method deletes the Request object'''
        del self.req
        print("Tests run, all variables have been deleted.")
        return

    def test_valid_input(self):
        '''Testing valid inputs for make_request'''

        # testing patents endpoint
        # ---> making api request
        self.req.make_request(
            endpoint='patents',
            query='{"assignee_country":["IT"]}',
            fields=["patent_id"]
        )
        # ---> checking the results
        result = ('{"patents":[{"patent_id":"10000041"},'
                  '{"patent_id":"10000044"},{"patent_id":"10000101"},'
                  '{"patent_id":"10000272"},{"patent_id":"10000275"},'
                  '{"patent_id":"10000309"},{"patent_id":"10000335"},'
                  '{"patent_id":"10000365"},{"patent_id":"10000417"},'
                  '{"patent_id":"10000757"},{"patent_id":"10000893"},'
                  '{"patent_id":"10001329"},{"patent_id":"10001453"},'
                  '{"patent_id":"10001530"},{"patent_id":"10001603"},'
                  '{"patent_id":"10002672"},{"patent_id":"10002836"},'
                  '{"patent_id":"10002990"},{"patent_id":"10003002"},'
                  '{"patent_id":"10003051"},{"patent_id":"10003956"},'
                  '{"patent_id":"10004250"},{"patent_id":"10004251"},'
                  '{"patent_id":"10004476"},{"patent_id":"10004702"}],'
                  '"count":25,"total_patent_count":59177}')
        self.assertEqual(self.req._Request__data, json.loads(result))

    def test_wrong_input(self):
        '''Testing wrong-case inputs for make_request'''

        # testing wrong val input
        self.assertEqual(print_patents('IT', 'l'), 0)

    def test_corner_input(self):
        '''Testing corner-case inputs for make_request'''

        # testing request generating no data
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.req.make_request(
                query=('{"_and":[{"assignee_country":"AQ"}]}'),
                fields=["patent_id"]
            )

        warning = '\033[93mThere is no data for your query\x1b[37m\n'
        assert fake_stdout.getvalue() == warning


if __name__ == '__main__':
    unittest.main()
