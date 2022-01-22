from urllib.request import urlopen
import patentsview as api
import json
import sys

def stampa_brevetti(name, surname, val, contents):
    match val:
        case 'n':                                   # stampa numero di brevetti
            print('\nIl numero di brevetti di ' + name + ' ' + surname + ' è: ' + str(contents['count']));
            return 1;
        case 'p':                                   # stampa il titolo di ciascun brevetto
            lista = []
            for patent in contents['patents']:      # appendi tutti i brevetti ad una lista
                patent_name = patent['patent_title'];
                lista.append(patent_name);
            lista = sorted(list(dict.fromkeys(lista))); # pulisci la lista dai duplicati e mettila in ordine alfabetico
            print('\nI brevetti di ' + name + ' ' + surname + ' sono:\n');
            for p in lista:
                print(p);
            return 1;

def ottieni_brevetti(name, surname):

    req = api.Request()
    req.make_request(
        query=('{"_and":[{"inventor_first_name":["%s"]},'
               '{"inventor_last_name":["%s"]}]}')
               % (name,surname)
    )
    return req.get_data()
    # try:                                                    # chiamata alle API e traducila in stringa
    #     contents = urlopen('https://api.patentsview.org/patents/query?q={"_and":[{"inventor_first_name":["' + name + '"]},{"inventor_last_name":["' + surname + '"]}]}').read()
    #     contents = json.loads(contents)                     # converti in JSON
    # except HTTPError as e:                                  # catch errori HTTP
    #     print('Error code: ', e.code)
    # except URLError as e:                                   # catch errori URL
    #     print('Reason: ', e.reason)
    # else:
    #     return contents

name = []
val = 0;

if len(sys.argv) == 4:
    name = sys.argv[1]
    surname = sys.argv[2]
    val = sys.argv[3]
    stampa_brevetti(name, surname, val, ottieni_brevetti(name, surname));
else:
    while 1: # ciclo infinito, nel caso sbagliasse a digitare il nome dell'artista
        name = input("Inserisci il nome dell'artista: ")  # prendo il nome e cognome
        surname = input("Inserisci il cognome dell'artista: ")  # prendo il nome e cognome

        if (len(name) == 0) or (len(surname) == 0):                                           # se sbaglia cicla
            print("\nPer favore, inserisci il Nome e il Cognome dell'artista\n")

        else:
            contents = ottieni_brevetti(name, surname)
            exit_code = 0                                       # exit_code è un flag pe ciclare nel caso l'utent e sbagliasse richiesta (p/n)
            while 1:
                val = input("\nTrovato! Cosa vuoi sapere di questo artista?\n\nI brevetti oppure il numero di brevetti? [p/n]: ")
                exit_code = stampa_brevetti(name, surname, val, contents);
                if exit_code == 1:
                    break
                else:
                    print('\nMi dispiace, gli unici valori accettati sono "p" (per i brevetti) ed "n" (per il numero di brevetti)')
            if exit_code == 1:
                break

input("\nPress Enter to exit...")
exit()
