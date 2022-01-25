import argparse
import pycountry


def make_argparse():

    FUNCTIONS = [
        'growth',
        'patents_from_author',
        'patents_from_country',
        'world_map'
    ]

    parser = argparse.ArgumentParser()

    parser.add_argument('command', choices=FUNCTIONS)
    # general arguments
    parser.add_argument('-v', '--verbose', action='store_true')

    # arguments needed for growth
    country_codes = []
    for country in list(pycountry.countries):
        country_codes += [country.alpha_2]
    parser.add_argument('-c', '--country', choices=country_codes)
    parser.add_argument('-b', '--begin', type=int, choices=range(1976, 2022))
    parser.add_argument('-e', '--end', type=int, choices=range(1976, 2022))

    # arguments needed for world_map
    continents = ['world', 'north america', 'africa',
                  'south america', 'asia', 'europe']
    parser.add_argument(
        '-a',
        '--continent',
        choices=continents
        )

    # arguments needed for patents_from_country
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--number', action='store_true')
    group.add_argument('-p', '--patents', action='store_true')

    # arguments needed for patents_from_author
    parser.add_argument('-f', '--name')
    parser.add_argument('-s', '--surname')

    args = parser.parse_args()

    return args
