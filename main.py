from analyzer import growth
from analyzer import author_feature
from analyzer import country_feature
from argparse_patents import make_argparse

args = make_argparse()

match args.command:
    case 'growth':
        country = args.country
        begin = args.begin
        end = args.end
        if country is not None and begin is not None and end is not None:
            growth.growth(country, begin, end, args.verbose)
        else:
            print(('You must specify all the following options:\n'
                   '\t• -c, --country: alpha_2 code of the country\n'
                   '\t• -b, --begin: starting year\n'
                   '\t• -e, --end: ending year'
                   ))

    case 'patents_from_country':
        if args.country is not None and (args.number or args.patents):
            if args.number:
                country_feature.print_patents(args.country, 'n', args.verbose)
            elif args.patents:
                country_feature.print_patents(args.country, 'p', args.verbose)
        else:
            print(('You must specify all the following options:\n'
                   '\t• -c, --country: alpha_2 code of the country'
                   '\t• -n, --number or -p, --patents: choose n '
                   '(number of patents) or p (list of patents\' titles)'
                   ))

    case 'patents_from_author':
        if args.name is not None and (args.number or args.patents):
            if args.number:
                author_feature.print_patents(args.name, args.surname, 'n')
            elif args.patents:
                author_feature.print_patents(args.name, args.surname, 'p')
        else:
            print(('You must specify all the following options:\n'
                   '\t• -f, --name: name of the author\n'
                   '\t• -s, --surname: surname of the author\n'
                   '\t• -n, --number or -p, --patents: choose n '
                   '(number of patents) or p (list of patents\' titles)'
                   ))

    case 'world_map':
        if args.continent is not None:
            country_feature.world_map(args.continent, args.verbose)
