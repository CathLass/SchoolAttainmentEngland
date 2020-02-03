import pandas as pd

# the data that links Local Authority (LA) codes to actual LA names you can recognise
datapath = "./data/"
datafile = 'Local_Authority_Districts_December_2017_Names_and_Codes_in_the_United_Kingdom.csv'

def read_LA_codes():
    la_codes_file = datapath + datafile
    la_codes = pd.read_csv(la_codes_file,delimiter=',')

    return la_codes

def find_code(la_codes,name):
    filter = la_codes['LAD17NM'] == name
    code = la_codes[filter]['LAD17CD'].iloc[0]
    return code

def find_LA(la_codes,code):
    filter = la_codes['LAD17CD'] == code
    name = la_codes[filter]['LAD17NM'].iloc[0]
    return name
