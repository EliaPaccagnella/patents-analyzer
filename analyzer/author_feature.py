import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analyzer.patentsview as api


def print_patents(name, surname, output):
    """
    Print the patents' count or a list patents' names.

    Parameters
    ----------
    name    : the name of the author, used to introduce the result, and to
              find the patents using the function "obtain_patents"
    surname : the surname of the author, used like the previous paramenter
    output     : the parameter passed as argument, used to print the right
              result (eg. patents' count or the list of names)
        If "n" will print the count of author's patents, if "p" will print
        the list author's patents' name, else will show an error.
    """
    # validating inputs
    if name == '' or surname == '':
        return 0
    if name.isalpha() and surname.isalpha() and output.isalpha():

        req = api.Request()
        req.make_request(
            query=('{"_and":[{"inventor_first_name":["%s"]},'
                   '{"inventor_last_name":["%s"]}]}') % (name, surname)
        )
        contents = req.get_data()

        match output:
            # print number of patents
            case 'n':
                print('\nThe number of patents of ' +
                      name + ' ' + surname + ' is: ' + str(contents['count'])
                      )
                return 1
            # print the title of each patent
            case 'p':
                patents = []
                # append all the patents to a list
                for patent in contents['patents']:
                    patent_name = patent['patent_title']
                    patents.append(patent_name)
                # clean the list of duplicates and put it in alphabetical order
                patents = sorted(list(dict.fromkeys(patents)))
                print('\nI The Patents of ' + name + ' ' + surname + ' are:\n')
                for patent in patents:
                    print(patent)
                return 1
    else:
        return 0
