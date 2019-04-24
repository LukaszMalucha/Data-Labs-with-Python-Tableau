from django.shortcuts import render
from data_science.utils import skill_cleaner, database_upload, skill_compare
from .forms import SkillsForm


def ds_dashboard(request):
    """Data Science homepage"""

    # Helper function for database upload if necessary
    # database_upload()

    return render(request, "ds_dashboard.html")


def test_profile(request):
    """Test skillset view"""

    form = SkillsForm(request.POST)

    if request.method == 'POST':

        skillset = request.POST.get('skills')
        skills = skill_cleaner(skillset)
        results_dictionary, missing_dictionary = skill_compare(skills)

    else:

        results_dictionary = None
        missing_dictionary = None

    return render(request, "test_profile.html",
                  {'form': form, 'missing_dictionary': missing_dictionary, 'results_dictionary': results_dictionary})
