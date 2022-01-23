from types import NoneType
import pycountry
import plotly.graph_objects as go
import pandas as pd
from patentsview import api


def print_patents(st, val):

    """
    Return the list or the count of patents given an assignee's country
    fetched using the API of "patentsview.org".

    PARAMETERS:
    st     : the name of the assignee's country
    val       : the parameter passed as argument, used to print the right
                result (eg. patents' count or the list of patents' names)
                If val="n", will print the count of the patents,
                if val="p", will print the list of patents' names,
                else will show an error.
    """
    req = api.Request()
    req.make_request(query='{"assignee_country":["' + st + '"]}')
    contents = req.get_data()
    # contents = get_patents(st)
    if type(contents) != NoneType:
        match val:
            case 'n':
                if contents['total_patent_count'] > 0:
                    if contents['total_patent_count'] >= 100000:
                        print('\nThe amount of patents of ' +
                              pycountry.countries.get(alpha_2=str(st)).name +
                              'is more than 100.000')
                        return 100000
                    else:
                        print('\nThe amount of patents of ' +
                              pycountry.countries.get(alpha_2=str(st)).name +
                              ' is: ' + str(contents['total_patent_count']))
                        return contents['total_patent_count']
            case 'p':
                if contents['patents'] is not None:
                    lista = []
                    for patent in contents['patents']:
                        patent_name = patent['patent_title']
                        lista.append(patent_name)
                    lista = sorted(list(dict.fromkeys(lista)))
                    print('\nThe patents of ' +
                          pycountry.countries.get(alpha_2=str(st)).name +
                          ' are:\n')
                    for p in lista:
                        print(p)
                    return 1
            case _:
                print('The parameter is not correct, please use "n" ' +
                      'to print the amount of patents or "p" for the ' +
                      'list of patents')
                return 0
    print('No patent found, ' +
          'please check the country\'s name or try with another one.')
    return 0


def world_map():

     """
    Return a world map graph showing countries
    in different gradients of red, based on their
    amount of patents. 
    
    """