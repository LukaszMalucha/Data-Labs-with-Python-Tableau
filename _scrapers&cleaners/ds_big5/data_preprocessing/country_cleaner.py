# -*- coding: utf-8 -*-


import pandas as pd
import csv



dataset = pd.read_csv('apple_countries.csv',  encoding = "ISO-8859-1")
dataset = dataset['location'].value_counts()

dataset.to_csv('apple_countries_count.csv')