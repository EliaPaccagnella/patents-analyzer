
<h1>Index</h1>

- [1. What is patents analyzer?](#1-what-is-patents-analyzer)
- [2. How to get it](#2-how-to-get-it)
  - [2.1. Prerequisites:](#21-prerequisites)
- [3. Usage](#3-usage)
  - [3.1. Growth](#31-growth)
  - [3.2. Patent from author](#32-patent-from-author)
  - [3.3. Patents from country](#33-patents-from-country)
  - [3.4. World map](#34-world-map)
- [4. Testing](#4-testing)
  - [4.1. Coverage report](#41-coverage-report)
- [5. Technology used](#5-technology-used)
  - [5.1. API description](#51-api-description)
    - [5.1.1. Software limitations](#511-software-limitations)

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

## 3.1. Growth

The Growth feature will create a barplot based on the requested country, the beginning year and the ending year. It shows a simple visualization of a general trend of patent growth in a specific country in a particular range of years.

**Command**: `growth`

Options available:

    -c, --country [*]:
        alpha_2 code name of the desired country
    -b, --begin [*]:
        starting year
    -e, --end [*]:
        ending year

[*] Required options

**Usage example**:

    python main.py growth --country 'IT' --begin '2010' --end '2020'

This will ask for the graph showing patents growth in Italy (country code `IT`) between 2010 and 2020. The output should be as follows:

![Growth of patents in Italy from 2010 to 2020](https://user-images.githubusercontent.com/93975010/150977243-3d019089-9625-4f81-96e6-97e12be42771.png)

**Tip**: To find the country code of your interest you can use online tools like [IBAN country codes table](https://www.iban.com/country-codes).


## 3.2. Patent from author

**Command**: `patent_from_author`

Options available:

    -f, --name [*]:
        first name of the desired author
    -s, --surname [*]:
        last name of the desired author
    -n, --number [*m]:
        if the user wants the relative number of the patents in output
    -p, --patents [*m]:
        if the user wants the relative list of the patents’ names in output

[*] Required options

[*m] Mutually exclusive options options, one is required

**Usage example**:

    python main.py patents_from_author --name 'Scott' --surname 'Davidson' -n

This command returns the **number of patents** for the given author. Output is as follows:

    The number of patents of Scott Davidson is: 15

**Usage example 2**:

    python main.py patents_from_author --name 'Scott' --surname 'Davidson' -p

This command returns the list of the first 25 **patents’ titles** for the given author.  Output is as follows:

    I The Patents of Scott Davidson are:

    Fish tape leader with quick change coupling
    Haptically enabled dental modeling system
    Integrated electrostatic discharge and overcurrent device
    Integrated overcurrent and overvoltage apparatus for use in the protection of telecommunication circuits
    Lawn debris handling system
    Method and system for providing single sign-on user names for web cookies in a multiple user information directory environment
    Method for providing single sign-on user names for Web cookies in a multiple user information directory environment
    Modulation charging circuitry for battery charging
    Modulation charging circuitry for battery charging using a power source providing different levels of current
    Role-based display of document renditions for web conferencing
    Sports racket strings of a synthetic thermoplastic polymeric material
    System for providing single sign-on user names for web cookies in a multiple user information directory environment
    Systems for hybrid geometric/volumetric representation of 3D objects
    Voltage variable material for direct application and devices employing same

## 3.3. Patents from country

**Function name**: `patents_from_country`

Options available:

    -c, --country [*]:
        alpha_2 code name of the desired country
    -n, --number [*m]:
        if the user wants the relative number of the patents in output
    -p, --patents [*m]:
        if the user wants the relative list of the patents’ names in output
    -v, --verbose:
        prints out the results (advised to True)

[*] Required options

[*m] Mutually exclusive options options, one is required

**Usage example**:

    python main.py patents_from_country -c 'IT' -n -v

This command returns the **number of patents** for the given country (100’000 is the maximum value of accepted patents). Output is as follows:

    The amount of patents of Italy is: 59700

**Usage example 2**:

    python main.py patents_from_country -c 'IT' -p -v

This command returns the list of the first 25 **patents’ titles** for the given country. Output is as follows:

    The patents of Italy are:

    Aircraft hybrid flight control system
    Biological degradation of ochratoxin A into ochratoxin α
    Capsule for preparing beverages
    Firearm with change configuration detection system
    Fused cast refractory material based on aluminium oxide, zirconium dioxide and silicon dioxide, and use of such a material
    Gene vector
    Integrated electronic device for monitoring humidity and/or corrosion
    Labelling machine and method
    Linear guanidine derivatives, methods of preparation and uses thereof
    Machine for fitting and removing a tyre and method for operating the machine
    Machine for preparing and laying a bituminous carpet for closing micro-trenches
    Machine with improved thermal efficiency for the production and dispensing of chilled food products
    Memory device with progressive row reading and related reading method
    Method for making a decorative multilaminar veneer
    Method for performing a remote management of a multi-subscription SIM module
    Method of fabricating a semiconductor device and semiconductor product
    Optical multiplexer/demultiplexer device comprising Porro prisms
    Panel for making furnishings such as doors, boards, tables, furniture or the like
    Porous-silicon light-emitting device and manufacturing method thereof
    Portable ultrasound system alternatively attachable to table base and forearm contact part
    Pulley for high-efficiency winch
    Reading circuit with automatic offset compensation for a magnetic-field sensor, and related reading method with automatic offset compensation
    Silicon integrated bivalve thermoelectric generator of out-of-plane heat flux configuration
    System for the storage of electric energy for a vehicle with electric propulsion and presenting cylindrical chemical batteries embedded in a    support matrix
    Thermal acoustic insulation blankets

**Tip**: To find the country code of your interest you can use online tools like [IBAN country codes table](https://www.iban.com/country-codes).

## 3.4. World map

**Function name**: `world_map`

Options available:

    -a, --continent [*]:
        'world',  'north america',  'africa',  'south america',  'asia',  'europe'
    -v, --verbose:
        prints out all the data downloaded (advised to False)

[*] Required options

**Usage example**:

    python main.py world_map --continent 'south america'

The World Map feature will create different choropleth maps based on the requested continent, allowing for an easy visualization of the 3D patents filing distribution. Output is as follows:

![image](https://user-images.githubusercontent.com/93975010/150991731-f85a03a4-2667-4782-b7a0-283e2d524c37.png)

# 4. Testing

All the tests can be found within the tests folder in the GitHub repository. Here you can find 19 different tests organized into five python files:
- `test_author.py` : contains 3 tests on the author_feature.py module
- `test_country.py` : contains 3 tests on the print_patents function of the contry_feature.py module
- `test_growth.py` : contains 4 tests on the growth.py module
- `test_patentsview.py` : contains 6 tests on the patentsview.py module
- `test_world_map.py` : contains 3 tests on the world_map function within the country_feature.py module

To run all the tests together run the following code:

    python -m unittest discover tests -b -v

Run single module tests with:

    python -m unittest tests\test_patentsview.py -b -v

or

    python test_patentsview.py

Warning: testing the world_map function will require on average 250 seconds and will generate 5 graphs that will be opened in a new web browser tab by plotly.

## 4.1. Coverage report

A report of the coverage of all the tests can be generated using the python coverage package:

    coverage3 run -m unittest discover tests -b -v
    coverage html analyzer\author_feature.py analyzer\country_feature.py analyzer\growth.py analyzer\patentsview.py

This will generate an `htmlcov\index.html` file containing the coverage report of the tests as follows:

![image](https://user-images.githubusercontent.com/93975010/150993581-c5a3f9a1-c8a1-40b9-9c21-99b06d7bc6e6.png)

The modules on the left can be navigated to visualize which sections of the code were not tested or were excluded during the unit testing.

# 5. Technology used

The project has been developed making use of ```python``` as main programming language. Data instead was gathered trought the PatentsView API.

## 5.1. API description

The project makes use exclusively of data gathered through the public API "Patents View" by the US Patent and Trademark Office (look at the [API's documentation here](https://patentsview.org/apis/api-query-language)).
> The PatentsView API is intended to inspire the exploration and enhanced understanding of US intellectual property (IP) and innovation systems. The database driving the API is regularly updated and integrates the best available tools for inventor disambiguation and data quality control.
>
><p align="right"><i>source: <a href="https://patentsview.org/apis/purpose">patentsview.org/apis/purpose</a></i></p>

Thus, there are 3 main reasons for which we chose this API for our projects:

1. we wanted to challenge ourself in using an API instead of importing the data directly form a .csv or .xls dataset;
2. this API does not require authentication to request the data;
3. the API was designed to "inspire the exploration and enhanced understanding" of world's IP system;

### 5.1.1. Software limitations

The choice of this API imposes some limitations to our project:

- **Quantity of data**: every function can not return more than 100.000 patents per time.

- **Time constraints**: each function can use only data older than June 29, 2021.

- **Request constraints**: since the API used in this project does not require a key to access the data, there is a constraint of 45 requests per minute.

- **Test failures**: the API is updated once every quarter and thus the test created before the update will no more work once the updates are online (see [API FAQs](https://patentsview.org/apis/api-faqs#data-updates) for reference).
