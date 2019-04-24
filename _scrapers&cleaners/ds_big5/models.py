from django.db import models

class MySkills(models.Model):
    myskills = models.TextField()
    
    
class DataSkill(models.Model):
    dataskill = models.CharField(max_length=255, blank=True)
    percentage = models.DecimalField(max_digits=2, decimal_places = 0, default = 0)
    
    def __str__(self):
        return self.dataskill
        
        
def skill_cleaner(data):
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
        element = element.replace('Business Analytics', 'Business Analysis')
        element = element.replace('Data Analytics', 'Data Analysis')
        element = element.replace('Programming Languages', 'Programming')
        element = element.replace('Big Data Analytics', 'Big Data')
        element = element.replace('HTML5', 'HTML')
        element = element.replace('Microsoft Excel', 'Excel')
        element = element.replace('Java Programming', 'Java')
        element = element.replace('MySQL', 'SQL')
        element = element.replace('Sql', 'SQL')
        element = element.replace('Optimizations', 'Optimization')
        element = element.replace('Spark', 'Apache Spark')
        skills_cleaned.append(element)
    return  skills_cleaned
        
    
        