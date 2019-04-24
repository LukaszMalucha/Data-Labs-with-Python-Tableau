import pandas as pd



def clean_dataset(filename):
    
    dataset = pd.read_csv(filename)
    dataset = dataset.iloc[:, [0,1,3,4,5,6,7]]
    dataset = dataset.dropna()
    dataset = dataset[dataset.ber_rating != 'BER SINo666of2006exempt']
    dataset = dataset[dataset.price != 'Price On Application']
    dataset = dataset[dataset.price != 'price']
    dataset = dataset.drop_duplicates()
    property_name = dataset['property_name']

    rows = []
    for row in property_name:
        row = row.split(', Co. ')[0]
        row = row.split(',')[-1]
        rows.append(row)

    
    dataset['area'] = rows 
    dataset['area'] = dataset['area'].str.lstrip()

    
    ## BER

    dataset['ber_rating'] = dataset['ber_rating'].str.replace('BER','')
    dataset['ber_rating'] = dataset['ber_rating'].str.replace(' ','')
    
    
    ## property type (1 - house, 0 - apartment)
    
    dataset.property_type.unique()
    
    dataset = dataset.replace('Apartment For Sale ', 'Apartment')
    dataset = dataset.replace('Duplex For Sale ', 'Apartment')
    dataset = dataset.replace('Detached House ', 'House')
    dataset = dataset.replace('End of Terrace House ', 'House')
    dataset = dataset.replace('Terraced House ', 'House')
    dataset = dataset.replace('ungalow For Sale ', 'House')
    dataset = dataset.replace('Semi-Detached House ', 'House')
    dataset = dataset.replace('partment for sale', 'Apartment')
    dataset = dataset.replace('uplex for sale', 'Apartment')
    dataset = dataset.replace('Detached House', 'House')
    dataset = dataset.replace('End of Terrace House', 'House')
    dataset = dataset.replace('Terraced House', 'House')
    dataset = dataset.replace('ungalow for sale', 'House')
    dataset = dataset.replace('Semi-Detached House', 'House')
    dataset = dataset.replace('Townhouse', 'House')
    dataset = dataset.replace('tudio apartment for sale', 'Apartment') 
    dataset = dataset.replace('House For Sale', 'House') 
    dataset = dataset.replace('Studio Apartment For Sale', 'Apartment')
    dataset = dataset.replace('Apartment', 0)
    dataset = dataset.replace('House', 1)
    
    ## beds
    dataset['beds'] = dataset['beds'].str.replace('Beds', '')
    dataset['beds'] = dataset['beds'].str.replace('Bed', '')
    dataset['beds'] = dataset['beds'].str.replace(' ','')
    
    ## baths
    dataset['baths'] = dataset['baths'].str.replace('Baths', '')
    dataset['baths'] = dataset['baths'].str.replace('Bath', '')
    dataset['baths'] = dataset['baths'].str.replace(' ','')
    
    ## price
    dataset['price'] = dataset['price'].str.replace('AMV: ', '')
    dataset['price'] = dataset['price'].str.replace(' ', '')
    
    dataset = dataset.rename(index=str, columns={'property_name': 'property address', 
                                             'property_type': 'type of property',
                                             'beds': 'bedrooms', 
                                             'baths': 'bathrooms', 
                                             'ber_rating': 'BER'})
    
    return dataset
    



    
cork_actual_clean = clean_dataset('cork_actual.csv')
cork_actual_clean.to_csv('cork_actual_address_clean.csv', encoding="utf-8")

galway_actual_clean = clean_dataset('galway_actual.csv')
galway_actual_clean.to_csv('galway_actual_address_clean.csv', encoding="utf-8")

limerick_actual_clean = clean_dataset('limerick_actual.csv')
limerick_actual_clean.to_csv('limerick_actual_address_clean.csv', encoding="utf-8")

#
#    
#    
import pandas as pd 
    
    
dataset = pd.read_csv('galway_actual.csv')
dataset = dataset.iloc[:, [0,1,3,4,5,7]]
dataset = dataset.dropna()
dataset = dataset.drop_duplicates()
#
#dataset = dataset[dataset.ber_rating != 'SINo666of2006exempt']
#dataset = dataset[dataset.price != 'Price On Application']
#
### property name  --> area address
#
#property_name = dataset['property_name']
#
#
#rows = []
#for row in property_name:
#    row = row.split(', Co. Galway')[0]
#    row = row.split(',')[-1]
#    rows.append(row)
#    
#address = pd.Series(rows) 
#
#dataset['area'] = rows  
#
#
### BER
#
#dataset['ber_rating'] = dataset['ber_rating'].str.replace('BER','')
#dataset['ber_rating'] = dataset['ber_rating'].str.replace(' ','')
#
#
### property type
#
#dataset.property_type.unique()
#
#dataset = dataset.replace('Apartment For Sale ', 'Apartment')
#dataset = dataset.replace('Duplex For Sale ', 'Apartment')
#dataset = dataset.replace('Detached House ', 'House')
#dataset = dataset.replace('End of Terrace House ', 'House')
#dataset = dataset.replace('Terraced House ', 'House')
#dataset = dataset.replace('ungalow For Sale ', 'House')
#dataset = dataset.replace('Semi-Detached House ', 'House')
#dataset = dataset.replace('partment for sale', 'Apartment')
#dataset = dataset.replace('uplex for sale', 'Apartment')
#dataset = dataset.replace('Detached House', 'House')
#dataset = dataset.replace('End of Terrace House', 'House')
#dataset = dataset.replace('Terraced House', 'House')
#dataset = dataset.replace('ungalow for sale', 'House')
#dataset = dataset.replace('Semi-Detached House', 'House')
#dataset = dataset.replace('Townhouse', 'House')
#dataset = dataset.replace('tudio apartment for sale', 'Apartment')
#
### beds
#dataset['beds'] = dataset['beds'].str.replace('Beds', '')
#dataset['beds'] = dataset['beds'].str.replace('Bed', '')
#dataset['beds'] = dataset['beds'].str.replace(' ','')
#
### baths
#dataset['baths'] = dataset['baths'].str.replace('Baths', '')
#dataset['baths'] = dataset['baths'].str.replace('Bath', '')
#dataset['baths'] = dataset['baths'].str.replace(' ','')
#
### price
#dataset['price'] = dataset['price'].str.replace('AMV: ', '')
#dataset['price'] = dataset['price'].str.replace(' ', '')
#
#dataset = dataset.rename(index=str, columns={'property_name': 'property address', 
#                                             'property_type': 'type of property',
#                                             'beds': 'bedrooms', 
#                                             'baths': 'bathrooms', 
#                                             'ber_rating': 'BER'})
#    
#
#
