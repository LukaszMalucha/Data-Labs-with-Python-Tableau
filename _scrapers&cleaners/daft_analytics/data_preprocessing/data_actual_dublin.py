import pandas as pd



def clean_dataset(filename):
    
    dataset = pd.read_csv(filename)
    dataset = dataset.iloc[:, [0,1,3,4,5,6,7]]
    dataset = dataset.dropna()
    dataset = dataset[dataset.ber_rating != 'BER SINo666of2006exempt']
    dataset = dataset[dataset.price != 'Price On Application']
    dataset = dataset[dataset.price != 'price']
    dataset = dataset[dataset.price != 'price']
    dataset = dataset.drop_duplicates()
    property_name = dataset['property_name']
    rows = []
    for row in property_name:
        if ', Co. ' in row:
            row = row.split(', Co. ')[0]
            row = row.split(',')[-1]
        else: 
            row = row.split('Dublin')[1]
            if ',' in row:
                row = row.split(',')[0]
            row = 'Dublin' + row    
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
    dataset = dataset.replace('ouse for sale', 'House')
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



dublin_actual_clean = clean_dataset('dublin_actual.csv')
dublin_actual_clean.to_csv('dublin_actual_address_clean.csv', encoding="utf-8")





















