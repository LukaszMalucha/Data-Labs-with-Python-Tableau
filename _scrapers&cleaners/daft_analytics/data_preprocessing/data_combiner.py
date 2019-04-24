## Combine actual property offers with 1-year historical data

import pandas as pd


def combine_dataset(actual, sold):
    dataset_actual = pd.read_csv(actual)
    dataset_sold = pd.read_csv(sold)
    
    
    dataset_actual = dataset_actual.iloc[:,[3,4,5,7,8]]
    dataset_actual = dataset_actual[['area', 'type of property', 'bedrooms', 'bathrooms', 'price']]
    dataset_sold = dataset_sold.iloc[:,1:]
    
    dataset_new = dataset_actual.append(dataset_sold,  ignore_index=True)
    
    return dataset_new


cork_sales_2018 = combine_dataset('cork_actual_address_clean.csv', 'cork_sold_clean.csv')  
galway_sales_2018 = combine_dataset('galway_actual_address_clean.csv', 'galway_sold_clean.csv')  
limerick_sales_2018 = combine_dataset('limerick_actual_address_clean.csv', 'limerick_sold_clean.csv')  

cork_sales_2018.to_csv('cork_sales_2018.csv', encoding="utf-8")
galway_sales_2018.to_csv('galway_sales_2018.csv', encoding="utf-8")
limerick_sales_2018.to_csv('limerick_sales_2018.csv', encoding="utf-8")

dublin_sales_2018 = pd.read_csv('dublin_sold_clean.csv')
dublin_sales_2018 = dublin_sales_2018.iloc[:,1:6]
dublin_sales_2018 = dublin_sales_2018[['area', 'type of property', 'bedrooms', 'bathrooms', 'price']] 
dublin_sales_2018.to_csv('dublin_sales_2018.csv', encoding="utf-8")

