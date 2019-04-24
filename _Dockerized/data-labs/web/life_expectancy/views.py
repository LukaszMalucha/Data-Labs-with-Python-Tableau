from django.shortcuts import render


def life_expectancy(request):
    return render(request, "life_expectancy.html")