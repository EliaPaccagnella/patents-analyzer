from urllib.request import urlopen
import patentsview as api
import json
import sys



def print_patents(name, surname, val, contents):
    """
    Print the patents' count or a list patents' names.

    Parameters
    ----------
    name    : the name of the author, used to introduce the result, and to
              find the patents using the function "obtain_patents"
    surname : the surname of the author, used like the previous paramenter
    val     : the parameter passed as argument, used to print the right
              result (eg. patents' count or the list of names)
        If "n" will print the count of author's patents, if "p" will print
        the list author's patents' name, else will show an error.
    contents: list of patents
    """

    match val:
        # print number of patents
        case 'n':
            print('\nThe number of patents of ' + name + ' ' + surname +
                  ' is: ' + str(contents['count']))
            return 1
        # print the title of each patent
        case 'p':
            lista = []
            # append all the patents to a list
            for patent in contents['patents']:
                patent_name = patent['patent_title']
                lista.append(patent_name)
            # clean the list of duplicates and put it in alphabetical order
            lista = sorted(list(dict.fromkeys(lista)))
            print('\nI The Patents of ' + name + ' ' + surname + ' are:\n')
            for p in lista:
                print(p)
            return 1


def obtain_patents(name, surname):
"""
Return the list and the count of patents'
getted using the API of "patentsview.org".
The name and surname of the author will be sent to "api.patentsview.org",
the result will be readed and loaded in JSON format.

Parameters
----------
name     : the name of the author
surname  : the surname of the author
"""

    req = api.Request()
    req.make_request(
        query=('{"_and":[{"inventor_first_name":["%s"]},'
               '{"inventor_last_name":["%s"]}]}') % (name, surname)
    )
    return req.get_data()


name = []
val = 0

if len(sys.argv) == 4:
    name = sys.argv[1]
    surname = sys.argv[2]
    val = sys.argv[3]
    print_patents(name, surname, val, obtain_patents(name, surname))
else:
    # infinite loop, in case you misspell the artist name
    while 1:
        # I take the name and surname
        name = input('Enter the artist name: ')
        surname = input('Enter the artist's surname: ')
        # if it makes a mistake, it cycles
        if (len(name) == 0) or (len(surname) == 0):
            print('\nPlease enter the Name and Surname of the artist\n')

        else:
            contents = obtain_patents(name, surname)
            # exit_code is a flag to cycle in case the user
            # gets the request wrong (p / n)
            exit_code = 0
            while 1:
                val = input('\nFound it! What do you want to know about this'
                            'artist?\n\nThe patents or the number of patents?'
                            '[p/n]: ')
                exit_code = print_patents(name, surname, val, contents)
                if exit_code == 1:
                    break
                else:
                    print('\n Sorry, the only accepted values are "p" (for'
                          'patents) and "n" (for number of patents)')
            if exit_code == 1:
                break

input('\nPress Enter to exit...')
exit()