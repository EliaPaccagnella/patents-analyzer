import json
import requests
from urllib.error import URLError, HTTPError
from analyzer.errors import errors


class Request():

    def __init__(self):
        self.__data = None

    def make_request(self, endpoint='patents',
                     query=None, fields='', verbose=True):

        '''Request data from the PatentsView API

    INPUT:
        • endpoint <str>: API endpoint to which you want to make requests.
                          Valid values are: ['patents','inventors','assignees',
                          'locations','cpc_subsections','uspc_mainclasses',
                          'nber_subcategories']
        • query <str>: query to the API as described in the API Documentation
        • fields <list>: fields to include in the results of the API

    OUTPUT:
        The function doesn't return directly the data. To obtain it, use the
        get_data method after making the request.
        If errors arise during the data request, this function will raise
        instead python errors signaling the issue.
        '''

        # defining basic URL syntax
        self.__request_url = ('https://api.patentsview.org/{endpoint}/'
                              'query?q={query}&f={fields}')

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
            if query is not None:
                # generating the request url
                self.__request_url = self.__request_url.format(
                    endpoint=endpoint,
                    query=query,
                    fields=str(fields).replace('\'', '"')
                )

                # making data request to the server
                try:
                    r = requests.get(self.__request_url).text
                    json_data = json.loads(r)
                # checking HTTP errors:
                except HTTPError as e:
                    if verbose:
                        print('HTTP Error code: ', e.code)
                    raise HTTPError
                # checking URL errors
                except URLError as e:
                    if verbose:
                        print('Reason: ', e.reason)
                    raise URLError

                # checking if there exists data with given requirements
                try:
                    if json_data['count'] == 0:
                        # there is no data for the query
                        # printing a small warning
                        if verbose:
                            print(('\033[93m'
                                   'There is no data for your query'
                                   '\033[37m'))
                        self.__data = json_data
                        return
                except KeyError:
                    if json_data['status'] == 'error':
                        # there was a syntax error either in fields or query
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
        """Returns the data generated with make_request.

        OUTPUT:
            data <json>: last API request outputed data
        """
        if self.__data is None:
            raise errors.NoData()
        return self.__data
