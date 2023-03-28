
from django.shortcuts import render


def filter(request):
    return render(request, "bestplan/filter.html")
