from urllib.request import urlopen
import patentsview as api
import json
import sys

def print_patents(name, surname, val, contents):
    match val:
        case 'n':                                   # print number of patents
            print('\nThe number of patents of ' + name + ' ' + surname + ' is: ' + str(contents['count']));
            return 1;
        case 'p':                                   # print the title of each patent
            lista = []
            for patent in contents['patents']:      # append all the patents to a list
                patent_name = patent['patent_title'];
                lista.append(patent_name);
            lista = sorted(list(dict.fromkeys(lista))); #clean the list of duplicates and put it in alphabetical order 
            print('\nI The Patents of ' + name + ' ' + surname + ' are:\n');
            for p in lista:
                print(p);
            return 1;

def obtain_patents(name, surname):

    req = api.Request()
    req.make_request(
        query=('{'_and':[{'inventor_first_name':['%s']},'
               '{'inventor_last_name':['%s']}]}')
               % (name,surname)
    )
    return req.get_data()
    # try:                                                    # call to the API and translate it to string
    #     contents = urlopen('https://api.patentsview.org/patents/query?q={'_and':[{'inventor_first_name':['' + name + '']},{'inventor_last_name':['' + surname + '']}]}').read()
    #     contents = json.loads(contents)                     # convert in JSON
    # except HTTPError as e:                                  # catch errors HTTP
    #     print('Error code: ', e.code)
    # except URLError as e:                                   # catch errors URL
    #     print('Reason: ', e.reason)
    # else:
    #     return contents

name = []
val = 0;

if len(sys.argv) == 4:
    name = sys.argv[1]
    surname = sys.argv[2]
    val = sys.argv[3]
    print_patents(name, surname, val, obtain_patents(name, surname));
else:
    while 1: # infinite loop, in case you misspell the artist name
        name = input('Enter the artist name: ')  # I take the name and surname
        surname = input('Enter the artist's surname: ')  # I take the name and surname

        if (len(name) == 0) or (len(surname) == 0):                                           # if it makes a mistake, it cycles
            print('\nPlease enter the Name and Surname of the artist\n')

        else:
            contents = obtain_patents(name, surname)
            exit_code = 0                                       # exit_code is a flag to cycle in case the user gets the request wrong (p / n)
            while 1:
                val = input('\nFound it! What do you want to know about this artist?\n\nThe patents or the number of patents?[p/n]: ')
                exit_code = print_patents(name, surname, val, contents);
                if exit_code == 1:
                    break
                else:
                    print('\n Sorry, the only accepted values ​​are 'p' (for patents) and 'n' (for number of patents)')
            if exit_code == 1:
                break

input('\nPress Enter to exit...')
exit()
