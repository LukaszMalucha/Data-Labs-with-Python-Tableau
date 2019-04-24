from django.shortcuts import render, redirect
from django.urls import reverse

from .utils import cork_areas, dublin_areas, galway_areas, limerick_areas, types, cork_path, dublin_path, galway_path, \
    limerick_path, price_regressor


def daft_dashboard(request):
    return render(request, "daft_dashboard.html")


def city_choice(request):
    if request.method == 'POST':
        request.session['city'] = request.POST['city']
        return redirect(reverse('daft_analytics:price_estimator'))

    return render(request, "city_choice.html")


def price_estimator(request):
    city = request.POST.get('city')
    if city == "Cork":
        areas = cork_areas
        dataset = cork_path
    elif city == "Dublin":
        areas = dublin_areas
        dataset = dublin_path
    elif city == "Galway":
        areas = galway_areas
        dataset = galway_path
    else:
        areas = limerick_areas
        dataset = limerick_path

    property_types = types

    if request.method == 'POST':
        area = request.POST['area']
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


    return render(request, "price_estimator.html", {'areas': areas, 'property_types': property_types, 'city': city, 'estimators': estimators})
