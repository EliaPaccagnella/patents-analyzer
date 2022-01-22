import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from patentsview import Request


def patents_country_years(country, start, end):
    data = {}
    if start > 1975 and end < 2022:
        if start > end:
            start, end = end, start
        for year in range(start, end+1):
            req = Request()
            query = '{"_and":[{"assignee_country": "'\
                    + country\
                    + '"}, {"patent_year": '\
                    + str(year)\
                    + '}]}'
            req.make_request('patents', query)
            contents = req.get_data()['total_patent_count']
            if contents != 0:
                data[str(year)] = contents

            # if the country is wrong:
            else:
                response = ('\033[93mSadly, there is no data for country {c}.'
                            '\033[37m').format(c=country)
                print(response)
                return response
        return data

    # if start and end are out of available range
    else:
        response = ('\033[93mPlease make sure: '
                    'starting year > 1975 and ending year < 2022.\033[37m')
        print(response)
        return response


def get_graph(dictionary, country, start, end):

    plt.bar(*zip(*dictionary.items()), color="lightpink")
    plt.ylabel('N. of new patents')
    plt.xlabel('Years')
    plt.title('Growth of patents in {c} from {s} to {e}'
              .format(c=country, s=start, e=end))
    # to get labels on the bars
    k = list(dictionary.keys())
    v = list(dictionary.values())
    for i in range(len(v)):
        plt.annotate(v[i], xy=(k[i], v[i]), ha='center', va='bottom')
    plt.show()


def growth(country, start, end):

    data = patents_country_years(country, start, end)
    if type(data) is dict:
        get_graph(data, country, start, end)

    return
