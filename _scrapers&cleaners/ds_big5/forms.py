from django import forms
from django.forms import ModelForm, Textarea
from .models import MySkills




class SkillsForm(forms.ModelForm):
    
    class Meta:
        model = MySkills
        fields = ['myskills']
        widgets = {
            'myskills': forms.Textarea(),
        }