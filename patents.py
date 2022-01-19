import json, requests


def get_patent(ID, verbose=True):
    link = 'https://api.patentsview.org/patents/query?q={"patent_number":"%s"}'
    r = requests.get(link % ID).text
    print (type(r))
    # checking if the it exists a patent with this ID
    data = json.loads(r)
    if data['count'] > 0:
        data = data['patents'][0]
        p_number = float(data['patent_number'])
        p_title = data['patent_title']
        if verbose:
            print(
                'The patent ID',
                ID,
                'corresponds with the patent number',
                p_number
            )
            print("Patent's title is:", p_title)
    else: return 'Patent missing'
    return p_number, p_title