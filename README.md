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
