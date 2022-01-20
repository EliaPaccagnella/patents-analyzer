import json, requests
import pandas as pd

from analyzer.errors import errors

class Request():

    def __init__(self):
        self.__data = None

    def make_request(self, endpoint='patents', query='', fields=None):
        # defining basic URL syntax
        self.__request_url = 'https://api.patentsview.org/{endpoint}/query?q={query}&f={fields}'
        
        # defining validation variables
        valid_endpoints = ['patents',
                           'inventors',
                           'assignees',
                           'locations',
                           'cpc_subsections',
                           'uspc_mainclasses',
                           'nber_subcategories']

        # checking endpoint validity
        if endpoint in valid_endpoints:
            if query != '':
                # generating the request url
                self.__request_url = self.__request_url.format(
                    endpoint=endpoint,
                    query=query,
                    fields=str(fields).replace('\'', '"')
                )

                # making data request to the server
                r = requests.get(self.__request_url).text
                json_data = json.loads(r)

                # checking if there exists data with given requirements
                try:
                    if json_data['count'] == 0:
                        # there is no data for the query
                        print(('\033[93m'
                               'There is no data for your query'
                               '\x1b[37m'))
                        self.__data = json_data
                        return
                except KeyError:
                    if json_data['status'] == 'error':
                        # there was a syntax error
                        raise errors.SyntaxError(
                            json_data['payload']['error']
                        )
                    else:
                        KeyError
                else:
                    self.__data = json_data
            else:
                raise errors.MissingQuery()
        else:
            raise errors.InvalidEndpoint(endpoint)

        return

    def get_data(self):
        if self.__data is None:
            raise errors.NoData()
        return self.__data
