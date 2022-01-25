# 1. What is patents analyzer?

Patents analyzer is a software for the analysis of world's patents. This software was developed by a group of five univeristy students entirely in python.

Patents analyzer allows to make analysis trought the request of both raw data and data visualization on 3D patents. The whole project is based on the USTPO's [PatentsView API](https://patentsview.org/apis/purpose).

# 2. How to get it

To use Patents Analyzer make sure your system satifies all the prerequisites and make a copy of this repository by copy-pasting this command in your terminal:
```
git clone https://github.com/EliaPaccagnella/patents-analyzer.git
cd patents-analyzer
```

## 2.1. Prerequisites:

In order to use `patents-analyzer` you need to have installed on your machine:

- [git](https://git-scm.com/downloads)
- [python v3.10](https://www.python.org/downloads/release/python-3100/)

Moreover, you will need the following python packages:

    pip install pycountry
    pip install plotly
    pip install pandas
    pip install matplotlib
    pip install tqdm
    pip install json
    pip install requests
    pip install unittest
    pip install argparse

# 3. Usage

This software was developed to be used directly from the terminal by developers or by importing it as a python library.

To run the program you need to launch the ```main.py``` file with the following command:

    python main.py COMMAND [options]

    COMMAND:
        growth
          |_ options:
                -c, --country: alpha_2 code name of the desired country
                -b, --begin: starting year
                -e, --end: ending year
        patents_from_author
          |_ options:
                -f, --name: first name of the desired author
                -s, --surname: last name of the desired author
                -n: if the user wants the relative number of the patents in output
                -p: if the user wants the relative list of the patents’ names in output
        patents_from_country
          |_ options:
                -c, --country: alpha_2 code name of the desired country
                -n: if the user wants the relative number of the patents in output
                -p: if the user wants the relative list of the patents’ names in output
                -v: prints out the results (advised to True)
        world_map
          |_ options:
                -a, --continent: 'world',  'north america',  'africa',  'south america', 'asia',  'europe'
                -v, --verbose: prints out all the data downloaded (advised to False)

The following sections show some usage examples for each command available.
