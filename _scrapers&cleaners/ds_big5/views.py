from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404  
from django.utils import timezone
from .forms import SkillsForm
from .models import MySkills, DataSkill, skill_cleaner
import pandas as pd


def ds_dashboard(request):
    
    return render(request, "ds_dashboard.html")
    

## Receiving User Skills
    
def data_skillset(request):
    
    form = SkillsForm(request.POST)
    
    if request.method == 'POST':
        
        if form.is_valid():
            request.session['myskills'] = request.POST['myskills']
            request.session['filename'] = 'media/ds_big5/skills_count.csv'
    
            return redirect(reverse('results'))
    
    return render(request, "data_skillset.html", {'form': form})
    
    
## Processing User Skills    
    
def results(request):
    
    skills = request.session.get('myskills')
    skills = skill_cleaner(skills)
    filename = request.session.get('filename')
    
    
    dataskills = pd.read_csv(filename)

    ## Skills Matching     
    
    results = dataskills[dataskills['dataskill'].isin(skills)]
    results = results.iloc[:,[0,1]]
    results = results.sort_values(by='percentage' , ascending=False)
    results.set_index('dataskill', inplace=True)
    results_dictionary = results.to_dict()
    results_dictionary = results_dictionary['percentage']
    
    ## Skills Missing
    missing =  dataskills[~dataskills['dataskill'].isin(skills)]
    missing = missing.iloc[:,[0,1]]
    missing = missing.sort_values(by='percentage' , ascending=False)[0:20]
    missing.set_index('dataskill', inplace=True)
    missing_dictionary = missing.to_dict()
    missing_dictionary = missing_dictionary['percentage']
    


    return render(request, "results.html",  { 'missing_dictionary': missing_dictionary, 'results_dictionary': results_dictionary })    
    
    
## Sample skillset:     
# Project Management,Data Visualization,Business Analysis,Agile Methodologies,Agile Project Management,
# Data Modeling,Statistical Data Analysis,Start-ups,Machine Learning,ETL,Data Mining,Analytics,SQL,JIRA,R,
# Microsoft Office,Representational State Transfer (REST),Microsoft Excel    