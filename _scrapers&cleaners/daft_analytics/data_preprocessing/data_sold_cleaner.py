import pandas as pd


def clean_dataset(filename):
    
    
    dataset = pd.read_csv(filename)
    dataset = dataset.iloc[:,[2,3,4,5,8]]
    dataset = dataset.dropna()
    
    ## Remove uncategorized data
        
    dataset = dataset[dataset.property_type != 'Site For Sale']
    dataset = dataset[dataset.property_type != 'Site For Sale ']
    dataset = dataset[dataset.property_type != 'Second-Hand Dwelling House/Apartment']
    dataset = dataset[dataset.property_type != 'New Dwelling House/Apartment']
    
    
    
    ## property_type(1-house, 0-apartment)
    dataset = dataset.replace('Apartment For Sale ', 'Apartment')
    dataset = dataset.replace('Duplex For Sale ', 'Apartment')
    dataset = dataset.replace('Detached House ', 'House')
    dataset = dataset.replace('End of Terrace House ', 'House')
    dataset = dataset.replace('Terraced House ', 'House')
    dataset = dataset.replace('Bungalow For Sale ', 'House')
    dataset = dataset.replace('Semi-Detached House ', 'House')
    dataset = dataset.replace('Townhouse', 'House')
    dataset = dataset.replace('Townhouse ', 'House')
    dataset = dataset.replace('Studio Apartment For Sale', 'Apartment')
    dataset = dataset.replace('Studio Apartment For Sale ', 'Apartment')
    dataset = dataset.replace('ouse for sale', 'House')
    dataset = dataset.replace('House For Sale', 1)
    dataset = dataset.replace('House For Sale ', 1)
    dataset = dataset.replace('House', 1)
    dataset = dataset.replace('Apartment', 0)
    
    ## beds
    dataset['beds'] = dataset['beds'].str.replace('Bedrooms', '')
    dataset['beds'] = dataset['beds'].str.replace('Bedroom', '')
    dataset['beds'] = dataset['beds'].str.replace(' ','')
    
    ## baths
    dataset['baths'] = dataset['baths'].str.replace('Bathrooms', '')
    dataset['baths'] = dataset['baths'].str.replace('Bathroom', '')
    dataset['baths'] = dataset['baths'].str.replace(' ','')
    
    
    ## price
    dataset['price'] = dataset['price'].str.replace(',', '')
    dataset['price'] = dataset['price'].str.replace('€', '')
    dataset['price'] = dataset['price'].str.replace(' ', '')
    dataset['price'] = dataset['price'].str.replace('*', '')
    dataset['price'] = dataset['price'].str.replace('+', '')
    
    dataset = dataset.rename(index=str, columns={'address': 'area', 
                                         'property_type': 'type of property',
                                         'beds': 'bedrooms', 
                                         'baths': 'bathrooms', 
                                         'ber_rating': 'BER'})
    
    return dataset


## Cleaning Data


cork_sold_clean = clean_dataset('cork_sold.csv')
cork_sold_clean.to_csv('cork_sold_clean.csv', encoding="utf-8")

galway_sold_clean = clean_dataset('galway_sold.csv')
galway_sold_clean.to_csv('galway_sold_clean.csv', encoding="utf-8")

limerick_sold_clean = clean_dataset('limerick_sold.csv')
limerick_sold_clean.to_csv('limerick_sold_clean.csv', encoding="utf-8")

dublin_sold_clean = clean_dataset('dublin_sold.csv')
dublin_sold_clean.to_csv('dublin_sold_clean.csv', encoding="utf-8")



























