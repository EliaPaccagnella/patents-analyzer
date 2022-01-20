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
        result = ('{"patents":[{"patent_number":"10006771",'
                  '"patent_processing_time":"698","patent_kind":"B2"},'
                  '{"patent_number":"10011146",'
                  '"patent_processing_time":"1800","patent_kind":"B2"},'
                  '{"patent_number":"10050913",'
                  '"patent_processing_time":"1700","patent_kind":"B2"},'
                  '{"patent_number":"10064048",'
                  '"patent_processing_time":"235","patent_kind":"B1"},'
                  '{"patent_number":"10067572",'
                  '"patent_processing_time":"2665","patent_kind":"B2"},'
                  '{"patent_number":"10157373",'
                  '"patent_processing_time":"497","patent_kind":"B1"},'
                  '{"patent_number":"10157374",'
                  '"patent_processing_time":"160","patent_kind":"B1"},'
                  '{"patent_number":"10169528",'
                  '"patent_processing_time":"2114","patent_kind":"B2"},'
                  '{"patent_number":"10182341",'
                  '"patent_processing_time":"351","patent_kind":"B2"},'
                  '{"patent_number":"10210177",'
                  '"patent_processing_time":"894","patent_kind":"B2"},'
                  '{"patent_number":"10237724",'
                  '"patent_processing_time":"755","patent_kind":"B2"},'
                  '{"patent_number":"10258654",'
                  '"patent_processing_time":"568","patent_kind":"B2"},'
                  '{"patent_number":"10274407",'
                  '"patent_processing_time":"354","patent_kind":"B2"},'
                  '{"patent_number":"10285100",'
                  '"patent_processing_time":"1477","patent_kind":"B2"},'
                  '{"patent_number":"10312419",'
                  '"patent_processing_time":"539","patent_kind":"B2"},'
                  '{"patent_number":"10321301",'
                  '"patent_processing_time":"1309","patent_kind":"B2"},'
                  '{"patent_number":"10325062",'
                  '"patent_processing_time":"844","patent_kind":"B2"},'
                  '{"patent_number":"10327140",'
                  '"patent_processing_time":"778","patent_kind":"B2"},'
                  '{"patent_number":"10335304",'
                  '"patent_processing_time":"1664","patent_kind":"B2"},'
                  '{"patent_number":"10339733",'
                  '"patent_processing_time":"575","patent_kind":"B2"},'
                  '{"patent_number":"10354469",'
                  '"patent_processing_time":"809","patent_kind":"B2"},'
                  '{"patent_number":"10382958",'
                  '"patent_processing_time":"1474","patent_kind":"B2"},'
                  '{"patent_number":"10391966",'
                  '"patent_processing_time":"775","patent_kind":"B2"},'
                  '{"patent_number":"10395449",'
                  '"patent_processing_time":"197","patent_kind":"B2"},'
                  '{"patent_number":"10395450",'
                  '"patent_processing_time":"197","patent_kind":"B2"}],'
                  '"count":25,"total_patent_count":484}')
        self.assertEqual(self.req._Request__data, json.loads(result))

        # testing inventors endpoint
        # ---> making api request
        self.req.make_request(
            endpoint='inventors',
            query='{"inventor_last_name":"Young"}',
            fields=["inventor_id"]
        )
        # ---> checking the results
        result = ('{"inventors":[{"inventor_id":"fl:t_ln:young-48"},'
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
                  '"count":25,"total_inventor_count":1952}')
        self.assertEqual(self.req._Request__data, json.loads(result))

        # testing assignees endpoint
        # ---> making api request
        self.req.make_request(
            endpoint='assignees',
            query='{"_begins":{"assignee_organization":"Race"}}',
            fields=["assignee_id"]
        )
        # ---> checking the results
        result = ('{"assignees":['
                  '{"assignee_id":"ef719d1c-52bd-4bcf-8a1e-1dba54f71f76"},'
                  '{"assignee_id":"688156dd-0ba8-488a-bf29-e748dc9f55b9"},'
                  '{"assignee_id":"ae884e9f-64ea-4c6a-b2d2-dc3f83a32f1f"},'
                  '{"assignee_id":"5ef1ebe7-93ba-4b8e-9c78-00227e355c99"},'
                  '{"assignee_id":"f1386c77-acb0-4fe1-9318-04fc3b6cb706"},'
                  '{"assignee_id":"1ee6c4dc-cba7-4cb1-a97b-ea1f363314df"},'
                  '{"assignee_id":"336378ae-dba8-46c8-a21c-a9fc9548e9a8"},'
                  '{"assignee_id":"05c63b8e-670d-445a-995a-df9d16adb8b0"},'
                  '{"assignee_id":"d0f5c21b-0559-44dd-ad13-169603968e32"},'
                  '{"assignee_id":"3855ccf0-089d-4d6d-a712-936263c7781f"},'
                  '{"assignee_id":"cb9a3fd3-2bb3-409c-9e23-0cb4c9e5250a"},'
                  '{"assignee_id":"84018e15-0b50-4c93-8300-a879eb08fbec"},'
                  '{"assignee_id":"757402a4-74fc-48f4-b466-592b4c0f966c"},'
                  '{"assignee_id":"764c39c7-574a-4d6d-85c2-cc9fc6a60705"},'
                  '{"assignee_id":"59d0e158-d526-4315-b0ec-c064253c75fb"},'
                  '{"assignee_id":"5c958e1d-f60a-4b25-ade1-810cef1522a8"},'
                  '{"assignee_id":"1adfdd0b-91c5-488b-aac1-724b1aad2700"},'
                  '{"assignee_id":"a0c79ab1-9507-4c6c-882e-0a99268aba7d"},'
                  '{"assignee_id":"99448ea6-4ece-4081-a19a-24c4ce9c9050"},'
                  '{"assignee_id":"20952a1d-62e3-4048-9bd3-68583c7b51e7"},'
                  '{"assignee_id":"76c0aff0-0d40-48c8-9204-9d043b8d9401"},'
                  '{"assignee_id":"1e810460-3ed0-4e00-94e7-d23a6960417c"},'
                  '{"assignee_id":"0722c2dd-9459-47cf-ba9b-891b140e7cd7"},'
                  '{"assignee_id":"2603e2be-a035-43cf-88b3-c25b7a5f09df"},'
                  '{"assignee_id":"0e4a8be0-77bd-47ff-ba66-2db32394cd65"}]'
                  ',"count":25,"total_assignee_count":36}')
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
