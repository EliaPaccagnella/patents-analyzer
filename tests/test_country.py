import unittest
import os
import sys
import json
from unittest.mock import patch
import io
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from patent import errors
from patent import api


class TestMakeRequestCountry(unittest.TestCase):

    def setUp(self):
        self.req = api.Request()
        print("\nInitializing test varibles...")
        return

    def tearDown(self):
        del self.req
        print("Tests run, all variables have been deleted.")
        return

    def test_valid_input(self):
        self.req.make_request(
            endpoint='patents',
            query='{"assignee_country":["IT"]}',
            fields=["patent_id"]
        )

        result = ('{"patents":[{"patent_id":"10000041"},{"patent_id":"10000044"},{"patent_id":"10000101"},{"patent_id":"10000272"},{"patent_id":"10000275"},{"patent_id":"10000309"},{"patent_id":"10000335"},{"patent_id":"10000365"},{"patent_id":"10000417"},{"patent_id":"10000757"},{"patent_id":"10000893"},{"patent_id":"10001329"},{"patent_id":"10001453"},{"patent_id":"10001530"},{"patent_id":"10001603"},{"patent_id":"10002672"},{"patent_id":"10002836"},{"patent_id":"10002990"},{"patent_id":"10003002"},{"patent_id":"10003051"},{"patent_id":"10003956"},{"patent_id":"10004250"},{"patent_id":"10004251"},{"patent_id":"10004476"},{"patent_id":"10004702"}],"count":25,"total_patent_count":59177}')
        self.assertEqual(self.req._Request__data, json.loads(result))

    def test_corner_input(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.req.make_request(
                query=('{"_and":[{"assignee_country":"AQ"}]}'),
                fields=["patent_id"]
            )

        warning = '\033[93mThere is no data for your query\x1b[37m\n'
        assert fake_stdout.getvalue() == warning

if __name__ == '__main__':
    unittest.main()
