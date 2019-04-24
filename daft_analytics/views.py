from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .utils import cork_areas, dublin_areas, galway_areas, limerick_areas, types, cork_path, dublin_path, galway_path, \
    limerick_path, price_regressor


def daft_dashboard(request):
    return render(request, "daft_dashboard.html")


def price_estimator(request):

    if request.method == 'POST':

        city = request.POST.get('city')

        if city == "Cork":
            dataset = cork_path
            area = request.POST['cork_area']
        elif city == "Dublin":
            dataset = dublin_path
            area = request.POST['dublin_area']
        elif city == "Galway":
            dataset = galway_path
            area = request.POST['galway_area']
        else:
            dataset = limerick_path
            area = request.POST['limerick_area']

        estimated_type = request.POST['property_type']
        if estimated_type == "House":
            property_type = 1
        else:
            property_type = 0

        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        estimators = price_regressor(dataset, area, property_type, bedrooms, bathrooms)
        estimators = sorted(estimators, key=int)
    else:
        estimators = None


    return render(request, "price_estimator.html",
                  {'cork_areas': cork_areas, 'dublin_areas': dublin_areas, 'galway_areas': galway_areas,
                   'limerick_areas': limerick_areas, 'property_types': types, 'estimators': estimators})
