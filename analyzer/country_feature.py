from types import NoneType
import pycountry
import plotly.graph_objects as go
import pandas as pd
import sys
import os
# importing modules from analyzer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analyzer.patentsview as api


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
    # creating a list of countries based on alpha_2 code for compatibility
    country_codes = []
    for country in list(pycountry.countries):
        country_codes += [country.alpha_2]

    data = {"code": [], "number of patents": []}

    # using previous print_patents function to retrieve number of patents
    for state in country_codes:
        data['code'] += [pycountry.countries.get(alpha_2=state).alpha_3]
        data['number of patents'] += [print_patents(state, "n")]

    df = pd.DataFrame(data)
    df.to_csv("patents/data.csv")

    # df = pd.read_csv('patents/data.csv')

    # using plotly documentation  https://plotly.com/python/choropleth-maps/
    fig = go.Figure(data=go.Choropleth(
        locations=df['code'],  # Spatial coordinates
        z=df['number of patents'].astype(float),  # Data to be color-coded
        locationmode='ISO-3',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="Number of patents",
    ))

    fig.update_layout(
        title_text='Number of patents by state',
        geo_scope='world',  # map scope selection
    )

    fig.show()
