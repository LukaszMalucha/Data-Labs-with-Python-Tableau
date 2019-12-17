import os.path

import pandas as pd
from django.conf import settings

# FILE PATHS
my_path = os.path.abspath(os.path.dirname(__file__))
data_skills_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/data_science/skills_count.csv")


def skill_cleaner(data):
    """Data Cleaner for skills"""
    skills_cleaned = []
    data = data.split(',')
    for element in data:
        element = element.title()
        element = element.strip()
        element = element.replace('Agile Methodologies', 'Agile')
        element = element.replace('Agile Project Management', 'Agile')
        element = element.replace('Algorithm Design', 'Algorithms')
        element = element.replace('Algorithm Analysis', 'Algorithms')
        element = element.replace('Analytical Skills', 'Analytics')
        element = element.replace('Applied Mathematics', 'Mathematics')
        element = element.replace('Ai', 'AI')
        element = element.replace('Artificial Intelligence', 'AI')
        element = element.replace('Big Data Analytics', 'Big Data')
        element = element.replace('Big data', 'Big Data')
        element = element.replace('Business Analytics', 'Business Analysis')
        element = element.replace('Bi', 'BI')
        element = element.replace('Data Analytics', 'Data Analysis')
        element = element.replace('Java Programming', 'Java')
        element = element.replace('HTML5', 'HTML')
        element = element.replace('Latex', 'LaTeX')
        element = element.replace('Microsoft Excel', 'Excel')
        element = element.replace('matlab', 'Matlab')
        element = element.replace('MySQL', 'SQL')
        element = element.replace('Microsoft Office', 'Office 365')
        element = element.replace('Optimizations', 'Optimization')
        element = element.replace('Programming Languages', 'Programming')
        element = element.replace('Sql', 'SQL')
        element = element.replace('Spark', 'Apache Spark')
        element = element.replace('Sas', 'SAS')

        skills_cleaned.append(element)
    return skills_cleaned

def skill_compare(skills):

    dataskills = pd.read_csv(data_skills_path)

    ## Skills Matching
    results = dataskills[dataskills['dataskill'].isin(skills)]
    results = results.iloc[:, [0, 1]]
    results = results.sort_values(by='percentage', ascending=False)
    results.set_index('dataskill', inplace=True)
    results_dictionary = results.to_dict()
    results_dictionary = results_dictionary['percentage']

    ## Skills Missing
    missing = dataskills[~dataskills['dataskill'].isin(skills)]
    missing = missing.iloc[:, [0, 1]]
    missing = missing.sort_values(by='percentage', ascending=False)[0:20]
    missing.set_index('dataskill', inplace=True)
    missing_dictionary = missing.to_dict()
    missing_dictionary = missing_dictionary['percentage']

    return results_dictionary, missing_dictionary

