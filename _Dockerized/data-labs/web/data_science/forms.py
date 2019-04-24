from django import forms


class SkillsForm(forms.Form):
    skills = forms.CharField(widget=forms.Textarea)