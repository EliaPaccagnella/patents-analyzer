import argparse
from analyzer import growth
from analyzer import author_feature
from analyzer import country_feature
import pycountry

def make_argparse():

    FUNCTION_MAP = {
        'graph_growth': growth,
        'patents_from_author': author_feature.print_patents,
        'patents_from_country': country_feature.print_patents,
        'world_map': country_feature.world_map
    }

    parser = argparse.ArgumentParser()

    parser.add_argument('command', choices=FUNCTION_MAP.keys())

    # general arguments
    parser.add_argument('-v', '--verbose', action='store_true')

    # arguments needed for growth
    country_codes = []
    for country in list(pycountry.countries):
        country_codes += [country.alpha_2]
    parser.add_argument('-c', '--country', choices=country_codes)
    parser.add_argument('-s', '--start', type=int, choices=range(1976,2022))
    parser.add_argument('-e', '--end', type=int, choices=range(1976,2022))

    # arguments needed for world_map
    parser.add_argument(
        '-a',
        '--continent',
        choices=[
            'world',
            'north america'
            'africa',
            'south america',
            'asia',
            'europe'
            ]
        )
    
    # arguments needed for patents_from_country and patents_from_author
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--number', action='store_true')
    group.add_argument('-p', '--patents', action='store_true')

    args = parser.parse_args()

    return args