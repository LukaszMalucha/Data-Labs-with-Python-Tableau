# -*- coding: utf-8 -*-


import pandas as pd
import csv



### INDUSTRY KNOWLEDGE - 


dataset = pd.read_csv('apple_top_skills.csv',  encoding = "ISO-8859-1")
dataset['skills'] = dataset['skills'].str.replace("[", "")
dataset['skills'] = dataset['skills'].str.replace("]", "")
dataset['skills'] = dataset['skills'].str.replace("'", "")

dataset.to_csv('apple_top_skills_clean.csv')


### COUNTING WORD OCCURENCE

dataset = pd.read_csv('apple_industry_knowledge_clean.csv',  encoding = "ISO-8859-1")


words= []
with open('apple_tools_and_technologies_clean.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
         csv_words = row[1].split(",")
         for i in csv_words:
              words.append(i)

words_counted = []
for i in words:
    x = words.count(i)
    words_counted.append((i,x))
    
words_count = list(set(words_counted))   


with open('apple_tools_and_technologies_count.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(words_count)






















dataset.to_csv('apple_skills.csv')





### COUNTRIES (APPLE ONLY)



countries = pd.read_csv('apple_countries.csv')
countries = countries.dropna()
countries = countries.ix[:,0]
countries.reset_index()

dataset['country'] = countries
dataset = dataset.reset_index()