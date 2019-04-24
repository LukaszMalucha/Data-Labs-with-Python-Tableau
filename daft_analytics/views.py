from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .utils import cork_areas, dublin_areas, galway_areas, limerick_areas, types, cork_path, dublin_path, galway_path, \
    limerick_path, price_regressor


def daft_dashboard(request):
    return render(request, "daft_dashboard.html")





def price_estimator(request):



    return render(request, "price_estimator.html",
                  {'cork_areas': cork_areas, 'dublin_areas': dublin_areas, 'galway_areas': galway_areas,
                   'limerick_areas': limerick_areas, 'property_types' : types})





