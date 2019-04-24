from django.shortcuts import render


def github_activity(request):
    return render(request, "github_activity.html")