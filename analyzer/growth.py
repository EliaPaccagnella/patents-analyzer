import sys
import os
import matplotlib.pyplot as plt
from tqdm import tqdm
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer.patentsview import Request

"""
you are interested in the growth of patents creation
of a specific country
in a specific period (years)
"""


def patents_country_years(country, start, end):

    """
    Given a country and a period of time, return a dictionary where:
    keys = year
    values = number of patents registered during the year

    Parameters:
    ----------
    country = a country in ISO 3166-1 alpha-2 (e.g. "US")
    start = the starting year of the period you are interested in (e.g. 1999)
            min value = 1976
            max value = 2021
    end = the ending year of the period you are interested in (e.g. 2007)
          min value = 1976
          max value = 2021
    """

    data = {}
    
    if start > end:
       start, end = end, start
    
    if start > 1975 and end < 2022:
        # implementing loading bar
        format = 'Loading data:\033[96m{bar:50}\033[37m {percentage:3.0f}%\n'
        for year in tqdm(range(start, end+1), bar_format=format):
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

    """
    Given a dictionary, return a barplot of the above data

    Parameters:
    ----------
    dictionary = output gained from the above function which type is dict
    country = a country in ISO 3166-1 alpha-2 (e.g. "US")
    start = the starting year of the period you are interested in (e.g. 1999)
            min value = 1976
            max value = 2021
    end = the ending year of the period you are interested in (e.g. 2007)
          min value = 1976
          max value = 2021
    """

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

    """
    Include the above 2 functions to have a better output

    Parameters:
    ----------
    country = a country in ISO 3166-1 alpha-2 (e.g. "US")
    start = the starting year of the period you are interested in (e.g. 1999)
            min value = 1976
            max value = 2021
    end = the ending year of the period you are interested in (e.g. 2007)
          min value = 1976
          max value = 2021
    """

    data = patents_country_years(country, start, end)
    if type(data) is dict:
        get_graph(data, country, start, end)

    return
