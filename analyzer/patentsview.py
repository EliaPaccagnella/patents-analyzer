import json, requests
import pandas as pd

class Request():

    def __init__(self):
        self.__request_url = 'https://api.patentsview.org/%s/query?'
        self.__data = None

    def make_request(self, endpoint='patents', query='', fields=None, verbose=0):
        # defining validation variables
        valid_endpoint = ['patents',
                          'inventors',
                          'assignees',
                          'location',
                          'CPC',
                          'USPC',
                          'NBER']

        if endpoint in valid_endpoint:
            # generating the request url
            self.__request_url = self.__request_url % endpoint
            self.__request_url += 'q=' + query
            if fields != None:
                self.__request_url += '&f=' + fields

            # making data request to the server
            r = requests.get(self.__request_url).text
            json_data = json.loads(r)

            # checking if there exists data with given requirements
            try:
                if json_data['count'] == 0:
                    # there is no data for the query
                    print('There is no data for your query')
                    return
            except KeyError:
                if json_data['status'] == 'error':
                    # probably there was a syntax error
                    print('\033[0;31m', json_data['payload']['error'], '\033[0;37m', sep='')
                else:
                    KeyError
            else:
                # data has been found
                # generating the pandas dataframe
                json_data = json_data[endpoint]
                self.__data = pd.DataFrame(columns=json_data[0].keys())
                print(self.__data.columns)
        else:
            print('''\033[0;31mError: {} is not a valid API endpoint
Try with one of the following values:
    •  'patents'
    •  'inventors'
    •  'assignees'
    •  'location'
    •  'CPC'
    •  'USPC'
    •  'NBER\033[0;37m'''.format(endpoint))
            return

        return

    def get_data(self):
        return self.__data  