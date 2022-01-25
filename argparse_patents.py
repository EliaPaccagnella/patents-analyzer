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

    parser.add_argument(
        'command',
        choices=FUNCTIONS,
        help=(
            'the command you want to use. Choices available are: '
            'growth, patents_from_author, patents_from_country, world_map'
        )
    )
    # general arguments
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help=(
            'increase output verbosity'
        )
    )

    # arguments needed for growth
    country_codes = []
    for country in list(pycountry.countries):
        country_codes += [country.alpha_2]
    parser.add_argument(
        '-c', '--country',
        choices=country_codes,
        help=(
            'country\'s ISO-3166 alpha 2 code. '
            'Find country codes in https://www.iban.com/country-codes'
        ),
        metavar=''
    )
    parser.add_argument(
        '-b', '--begin',
        type=int,
        choices=range(1976, 2022),
        help=(
            'starting year for the data visualization, '
            'must be between 1975 and 2022 (extremes excluded)'
        ),
        metavar=''
        )
    parser.add_argument(
        '-e', '--end',
        type=int,
        choices=range(1976, 2022),
        help=(
            'ending year for the data visualization, '
            'must be between 1975 and 2022 (extremes excluded)'
        ),
        metavar=''
    )

    # arguments needed for world_map
    continents = ['world', 'north america', 'africa',
                  'south america', 'asia', 'europe']
    parser.add_argument(
        '-a', '--continent',
        choices=continents,
        help=(
            'the continent you want to graph the distribution of patents. '
            'Valid continents are: \'world\', \'europe\', \'north america\', '
            '\'south america\', \'africa\', \'asia\'. '
            '\033[93mWarning: \'oceania\' is not available\033[37m.'
        ),
        metavar=''
    )

    # arguments needed for patents_from_country and patents_from_author
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-n', '--number',
        action='store_true',
        help=(
            'output the number of patents'
        )
    )
    group.add_argument(
        '-p', '--patents',
        action='store_true',
        help=(
            'output the list of the first 25 patents\' titles'
        )
    )

    # arguments needed for patents_from_author
    parser.add_argument(
        '-f', '--name',
        help=(
            'name of the patent author'
        ),
        metavar=''
    )
    parser.add_argument(
        '-s', '--surname',
        help=(
            'surname of the patent author'
        ),
        metavar=''
    )

    args = parser.parse_args()

    return args
