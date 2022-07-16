import pickle

# load data
with open('src/data.pickle', 'rb') as f:
    data = pickle.load(f)

# create columns
columns_cities = dict()
columns_cities['City'] = 'City'
columns_cities['1 bedroom flat'] = 'bd1a'
columns_cities['2 bedrooms flat'] = 'bd2a'
columns_cities['3 bedrooms flat'] = 'bd3a'
columns_cities['4 bedrooms house'] = 'bd4h'

columns_postcodes = dict()
columns_postcodes['Postcode'] = 'postcode'
columns_postcodes['1 bedroom flat'] = 'bd1a'
columns_postcodes['2 bedrooms flat'] = 'bd2a'
columns_postcodes['3 bedrooms flat'] = 'bd3a'
columns_postcodes['4 bedrooms house'] = 'bd4h'

