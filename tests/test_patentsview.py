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


class test_make_request(unittest.TestCase):

    def setUp(self):
        '''Before every test this method creates a new Request object'''
        self.req = api.Request()
        print("\nInitializing test...")
        return

    def tearDown(self):
        '''After every test, this method deletes the Request object'''
        del self.req
        print("Tests result:")
        return

    def test_valid_input(self):
        '''Testing valid inputs for make_request. Tests made are:
        • default endpoint + default fields
        • default endpoint (= patents)
        • patents endpoint
        • inventors endpoint
        • assignees endpoint
        • locations endpoint
        '''

        # testing input with only query specified
        self.req.make_request(query='{"patent_number":"7861215"}')
        result = ('{"patents":[{"patent_id":"7861215",'
                  '"patent_number":"7861215","patent_title":"Method,'
                  ' system, and program product for modeling processes"}],'
                  '"count":1,"total_patent_count":1}')
        self.assertEqual(self.req._Request__data, json.loads(result))

        # testing default endpoint
        # ---> making api request
        self.req.make_request(
            query='{"_and":[{"assignee_country":"IT"},{"patent_year":2020}]}',
            fields=["patent_id"]
        )
        # ---> checking the results
        result = ('{"patents":[{"patent_id":"10524528"},'
                  '{"patent_id":"10524914"},{"patent_id":"10525006"},'
                  '{"patent_id":"10525072"},{"patent_id":"10525161"},'
                  '{"patent_id":"10525429"},{"patent_id":"10525432"},'
                  '{"patent_id":"10525653"},{"patent_id":"10525755"},'
                  '{"patent_id":"10525948"},{"patent_id":"10525990"},'
                  '{"patent_id":"10526053"},{"patent_id":"10526156"},'
                  '{"patent_id":"10526365"},{"patent_id":"10526442"},'
                  '{"patent_id":"10526735"},{"patent_id":"10526781"},'
                  '{"patent_id":"10526794"},{"patent_id":"10526827"},'
                  '{"patent_id":"10526892"},{"patent_id":"10526926"},'
                  '{"patent_id":"10527052"},{"patent_id":"10527206"},'
                  '{"patent_id":"10527209"},{"patent_id":"10527259"}],'
                  '"count":25,"total_patent_count":2596}')
        self.assertEqual(self.req._Request__data, json.loads(result))

        # testing patents endpoint
        # ---> making api request
        self.req.make_request(
            endpoint='patents',
            query=(
                '{"_and": [{"_gte":{"patent_date":"2001-01-01"}},'
                '{"_text_any":{"patent_abstract":"international"}},'
                '{"_neq":{"assignee_lastknown_country":"US"}}]}'
            ),
            fields=[
                "patent_number",
                "patent_processing_time",
                "patent_kind"
            ]
        )
        # ---> checking the results
        result = (
            '{"patents":[{"patent_number":"10006771",'
            '"patent_processing_time":"698","patent_kind":"B2"},'
            '{"patent_number":"10011146","patent_processing_time":"1800",'
            '"patent_kind":"B2"},{"patent_number":"10050913",'
            '"patent_processing_time":"1700","patent_kind":"B2"},'
            '{"patent_number":"10067572","patent_processing_time":"2665",'
            '"patent_kind":"B2"},{"patent_number":"10157373",'
            '"patent_processing_time":"497","patent_kind":"B1"},'
            '{"patent_number":"10157374","patent_processing_time":"160",'
            '"patent_kind":"B1"},{"patent_number":"10169528",'
            '"patent_processing_time":"2114","patent_kind":"B2"},'
            '{"patent_number":"10182341","patent_processing_time":"351",'
            '"patent_kind":"B2"},{"patent_number":"10210177",'
            '"patent_processing_time":"894","patent_kind":"B2"},'
            '{"patent_number":"10237724","patent_processing_time":"755",'
            '"patent_kind":"B2"},{"patent_number":"10258654",'
            '"patent_processing_time":"568","patent_kind":"B2"},'
            '{"patent_number":"10274407","patent_processing_time":"354",'
            '"patent_kind":"B2"},{"patent_number":"10285100",'
            '"patent_processing_time":"1477","patent_kind":"B2"},'
            '{"patent_number":"10312419","patent_processing_time":"539",'
            '"patent_kind":"B2"},{"patent_number":"10321301",'
            '"patent_processing_time":"1309","patent_kind":"B2"},'
            '{"patent_number":"10325062","patent_processing_time":"844",'
            '"patent_kind":"B2"},{"patent_number":"10327140",'
            '"patent_processing_time":"778","patent_kind":"B2"},'
            '{"patent_number":"10335304","patent_processing_time":"1664",'
            '"patent_kind":"B2"},{"patent_number":"10339733",'
            '"patent_processing_time":"575","patent_kind":"B2"},'
            '{"patent_number":"10354469","patent_processing_time":"809",'
            '"patent_kind":"B2"},{"patent_number":"10382958",'
            '"patent_processing_time":"1474","patent_kind":"B2"},'
            '{"patent_number":"10395449","patent_processing_time":"197",'
            '"patent_kind":"B2"},{"patent_number":"10395450",'
            '"patent_processing_time":"197","patent_kind":"B2"},'
            '{"patent_number":"10395451","patent_processing_time":"197",'
            '"patent_kind":"B2"},{"patent_number":"10410179",'
            '"patent_processing_time":"837","patent_kind":"B2"}],'
            '"count":25,"total_patent_count":476}'
        )
        self.assertEqual(self.req._Request__data, json.loads(result))

        # testing inventors endpoint
        # ---> making api request
        self.req.make_request(
            endpoint='inventors',
            query='{"inventor_last_name":"Young"}',
            fields=["inventor_id"]
        )
        # ---> checking the results
        result = (
            '{"inventors":[{"inventor_id":"fl:t_ln:young-48"},'
            '{"inventor_id":"fl:j_ln:young-123"},'
            '{"inventor_id":"fl:r_ln:young-73"},'
            '{"inventor_id":"fl:r_ln:young-105"},'
            '{"inventor_id":"fl:j_ln:young-70"},'
            '{"inventor_id":"fl:t_ln:young-92"},'
            '{"inventor_id":"fl:f_ln:young-22"},'
            '{"inventor_id":"fl:v_ln:young-14"},'
            '{"inventor_id":"fl:r_ln:young-155"},'
            '{"inventor_id":"fl:d_ln:young-86"},'
            '{"inventor_id":"fl:a_ln:young-73"},'
            '{"inventor_id":"fl:k_ln:young-92"},'
            '{"inventor_id":"fl:c_ln:young-66"},'
            '{"inventor_id":"fl:j_ln:young-32"},'
            '{"inventor_id":"fl:d_ln:young-45"},'
            '{"inventor_id":"fl:j_ln:young-41"},'
            '{"inventor_id":"fl:j_ln:young-184"},'
            '{"inventor_id":"fl:j_ln:young-218"},'
            '{"inventor_id":"fl:m_ln:young-36"},'
            '{"inventor_id":"fl:c_ln:young-128"},'
            '{"inventor_id":"fl:c_ln:young-19"},'
            '{"inventor_id":"fl:b_ln:young-46"},'
            '{"inventor_id":"fl:w_ln:young-76"},'
            '{"inventor_id":"fl:t_ln:young-17"},'
            '{"inventor_id":"fl:w_ln:young-14"}],'
            '"count":25,"total_inventor_count":1964}'
        )
        self.assertEqual(self.req._Request__data, json.loads(result))

        # testing assignees endpoint
        # ---> making api request
        self.req.make_request(
            endpoint='assignees',
            query='{"_begins":{"assignee_organization":"Race"}}',
            fields=["assignee_id"]
        )
        # ---> checking the results
        result = (
            '{"assignees":['
            '{"assignee_id":"f397a05a-896d-43f4-8223-f251e28cac03"},'
            '{"assignee_id":"f0cb3bd6-d1f4-4bad-87d9-4747b3ba352f"},'
            '{"assignee_id":"425c27fc-ccc3-4663-b3c3-d2ef3b2d404e"},'
            '{"assignee_id":"6a684fa2-a929-4ae7-b845-6be6b21bad64"},'
            '{"assignee_id":"6d6559a7-777a-49c6-b9e2-e36a32774a41"},'
            '{"assignee_id":"6f93d51f-377b-4f33-b8cf-e3326b9a8706"},'
            '{"assignee_id":"165251ba-359d-4d2d-b11f-eb367b0c0d31"},'
            '{"assignee_id":"f0d968f0-8e6d-4d0e-a5df-c8fc6d27cd3d"},'
            '{"assignee_id":"b040caaa-5637-47e6-9a6c-1f14b7559c28"},'
            '{"assignee_id":"ae61403d-7c9a-49e3-961c-a30c690992eb"},'
            '{"assignee_id":"e2eb96bf-caa8-4e77-8587-27d542559b8a"},'
            '{"assignee_id":"3cddca88-0949-41a2-a9f9-5f9894fd5f43"},'
            '{"assignee_id":"6cfce6f2-6afd-408a-a73e-d89da50f3bf9"},'
            '{"assignee_id":"97ab8a08-0733-4a44-8eb3-6cddaf065b80"},'
            '{"assignee_id":"96a6943f-8d7f-455c-97ea-029c42ce79fb"},'
            '{"assignee_id":"2e49a438-bbfb-4c2c-9343-661b9429a842"},'
            '{"assignee_id":"2c4953e2-8302-4e27-bbe2-b9e4b3bdcb1e"},'
            '{"assignee_id":"118ac57a-60f9-4694-b1a8-0c53328ae72b"},'
            '{"assignee_id":"e1bfc0e0-03e8-49eb-8499-9c54e7070c75"},'
            '{"assignee_id":"45f96f16-0c1b-457a-9979-7b5551e7d3bb"},'
            '{"assignee_id":"f1927c05-da5e-42a8-a8c7-90ba16023a62"},'
            '{"assignee_id":"4b612f6e-9a99-4cec-9b97-2a22d3ccad6f"},'
            '{"assignee_id":"746abc96-0bfa-4141-ae43-2ead67f1227c"},'
            '{"assignee_id":"7a5744b8-828c-47c8-900b-cf144719f068"},'
            '{"assignee_id":"5ce7ffd5-3c95-4cfc-a35b-abe71a368363"}],'
            '"count":25,"total_assignee_count":36}'
        )
        self.assertEqual(self.req._Request__data, json.loads(result))

        # testing locations endpoint
        # ---> making api request
        self.req.make_request(
            endpoint='locations',
            query='{"location_city":"Mount Airy"}',
            fields=["location_id"]
        )
        # ---> checking the results
        result = ('{"locations":[{"location_id":"36.5027|-80.6179"},'
                  '{"location_id":"39.3809|-77.1511"}],'
                  '"count":2,"total_location_count":2}')
        self.assertEqual(self.req._Request__data, json.loads(result))

    def test_wrong_input(self):
        '''Testing invalid inputs for make_request. Tests made are:
        • wrong query syntax (misspelling and syntax structure errors)
        • wrong fields syntax (misspelling errors)
        • wrong fields syntax (syntax structure errors)
        • no query is specified
        • invalid endpoint
        '''

        # testing invalid query syntax
        with self.assertRaises(errors.SyntaxError):
            self.req.make_request(
               query=('{"_and:[{"assignee_country":"IT"},'  # missing closing "
                      '{"patent_year":2020}]}')
            )

        with self.assertRaises(errors.SyntaxError):
            self.req.make_request(
               query='{"patent_nuber":"7861215"}'          # misspelling number
            )

        # testing invalid field syntax
        with self.assertRaises(errors.SyntaxError):
            self.req.make_request(
               query=('{"_and:"[{"assignee_country":"IT"},'
                      '{"patent_year":2020}]}'),
               fields=["patnt_id"]                         # misspelling patent
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
        '''Testing corner-case inputs for make_request. Tests made are:
        • request is valid but generates no data
        '''

        # testing request generating no data
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.req.make_request(
                query=(
                    '{"_and":[{"inventor_first_name":["Scott"]},'
                    '{"inventor_last_name":["Davidson"]},'
                    '{"patent_year":2022}]}'
                ),
                fields=["patent_id"]
            )

        warning = '\033[93mThere is no data for your query\x1b[37m\n'
        assert fake_stdout.getvalue() == warning

        # testing for a statement beeing printed in the terminal
        # source: https://bit.ly/3mQUwsO


class test_get_data(unittest.TestCase):

    def setUp(self):
        '''Before every test, this method creates a new Request object'''
        self.req = api.Request()
        print("\nInitializing test...")
        return

    def tearDown(self):
        '''After every test, this method deletes the Request object'''
        del self.req
        print("Tests result")
        return

    def test_valid_input(self):
        '''Testing right usage of get_data.'''

        # testing correct functioning
        self.req.make_request(
            query='{"patent_number":"7861215"}'
        )
        self.assertEqual(self.req.get_data(), self.req._Request__data)

    def test_wrong_input(self):
        '''Testing get data call before to make a data request.'''

        # testing data request before using the make_request method
        with self.assertRaises(errors.NoData):
            self.req.get_data()

    def test_corner_input(self):
        '''Testing correct usage of get data in case
        the request previously made returns no data.'''

        # testing the case in which the make_request method returns no data
        self.req.make_request(
            query=('{"_and":[{"assignee_country":"IT"},'
                   '{"patent_year":2022}]}'),
            fields=["patent_id"]
        )
        self.assertEqual(self.req.get_data(), self.req._Request__data)


if __name__ == '__main__':
    unittest.main()
