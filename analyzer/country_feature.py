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
    # defining continents
    continents = {
        'world': ['*'],
        'north america': [
            'AG', 'BB', 'BS', 'BZ', 'CA', 'CR', 'CU', 'DM', 'DO', 'GT', 'GT',
            'HN', 'JM', 'MX', 'NI', 'PA', 'TT', 'US', 'SV', 'GD', 'KN',
            'LC', 'VC'
            ],
        'africa': [
            'AO', 'BF', 'BI', 'BJ', 'BW', 'CD', 'CG', 'CI', 'CM', 'CV', 'DJ',
            'EG', 'ER', 'ET', 'GA', 'GH', 'GM', 'GN', 'GW', 'KE', 'LR', 'LS',
            'LY', 'MG', 'ML', 'MR', 'MU', 'MW', 'MZ', 'NA', 'NE', 'NG', 'RW',
            'SC', 'SD', 'SL', 'SN', 'SO', 'ST', 'TG', 'TN', 'TZ', 'UG', 'ZM',
            'ZW', 'DZ', 'CF', 'TD', 'KM', 'GQ', 'MA', 'ZA', 'SZ'
            ],
        'south america': [
            'AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'GY', 'PE', 'PY', 'SR',
            'UY', 'VE'
            ],
        'asia': [
            'AF', 'AM', 'AZ', 'BD', 'BH', 'BN', 'BT', 'CN', 'CY', 'GE',
            'ID', 'IL', 'IN', 'IQ', 'IR', 'JO', 'JP', 'KG', 'KP', 'KR',
            'KW', 'LB', 'MM', 'MN', 'MV', 'MY', 'NP', 'OM', 'PH', 'PK',
            'QA', 'SA', 'SG',  'SY', 'TH', 'TJ',  'TM', 'TR', 'UZ', 'VN',
            'YE', 'KH', 'TL', 'KZ', 'LA', 'LK', 'AE'
            ],
        'europe': [
            'AD', 'AL', 'AT', 'BE', 'BG', 'BY',
            'CZ', 'DE', 'DK', 'EE', 'FI', 'FR',
            'GR', 'HU', 'IE', 'IS', 'IT', 'LI',
            'LT', 'LU', 'LV', 'MK', 'MT', 'NL',
            'NO', 'PL', 'PT', 'RO', 'RU', 'SE',
            'SI', 'SK', 'SM', 'UA', 'VA', 'BA',
            'HR', 'MD', 'MC', 'ME', 'RS', 'ES',
            'CH', 'GB'
            ]
        }

    continent = continent.lower()

    if continent in continents.keys():
        # creating a list of countries based on alpha_2 code for compatibility
        country_codes = []
        for country in list(pycountry.countries):
            country_codes += [country.alpha_2]

        data = {"code": [], "number of patents": []}

    # using previous print_patents function to retrieve number of patents
    for state in country_codes:
            if state in continents[continent] or continent == 'world':
                # adding country code to the data dictionary
                data['code'] +=
                [pycountry.countries.get(alpha_2=state).alpha_3]
                # using print_patents function to retrieve number of patents
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
        geo_scope=continent,  # sets the map to show th continent specified
    )

    fig.show()
    return 1
    else:
        print(('{continent} is not a valid continent. Choose among:\n'
               '\t- europe\n'
               '\t- north america\n'
               '\t- south america\n'
               '\t- asia\n'
               '\t- africa\n'
               '\t- world\n').format(continent=continent))
        return 0

