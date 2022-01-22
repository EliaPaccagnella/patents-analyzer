import unittest
import os
import sys
import json
from unittest.mock import patch
import io
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from patent import errors
from patent import api


class TestMakeRequestAuthor(unittest.TestCase):

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
            query='{"_and":['
                        '{"inventor_first_name":["Scott"]},'
                        '{"inventor_last_name":["Davidson"]}'
                  ']}',
            fields=["patent_id"]
        )

        # ---> checking the results
        result = ('{"patents":['
                        '{"patent_id":"4586708"},'
                        '{"patent_id":"6628498"},'
                        '{"patent_id":"6636404"},'
                        '{"patent_id":"7202770"},'
                        '{"patent_id":"7367600"},'
                        '{"patent_id":"7425815"},'
                        '{"patent_id":"7480718"},'
                        '{"patent_id":"7550948"},'
                        '{"patent_id":"7925752"},'
                        '{"patent_id":"8040345"},'
                        '{"patent_id":"8291088"},'
                        '{"patent_id":"8359114"},'
                        '{"patent_id":"8769006"},'
                        '{"patent_id":"9032028"},'
                        '{"patent_id":"9065262"}'
                '],'
                '"count":15,'
                '"total_patent_count":15}')
        self.assertEqual(self.req._Request__data, json.loads(result))

    def test_wrong_input(self):
        with self.assertRaises(errors.SyntaxError):
            self.req.make_request(
               query=('{"_and":['
                            '{"inventor_first_name":[Scott]},'
                            '{"inventor_last_name":[Davidson]},'
                            '{"patent_year":2022}'
                        ']}'),
               fields=["patent_id"]
            )

    def test_corner_input(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.req.make_request(
                query=('{"_and":['
                            '{"inventor_first_name":["Scott"]},'
                            '{"inventor_last_name":["Davidson"]},'
                            '{"patent_year":2022}'
                        ']}'),
                fields=["patent_id"]
            )

        warning = '\033[93mThere is no data for your query\x1b[37m\n'
        assert fake_stdout.getvalue() == warning

if __name__ == '__main__':
    unittest.main()
