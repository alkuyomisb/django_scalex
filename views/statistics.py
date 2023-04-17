from django.shortcuts import render
from utils.database_api import display_chart
def statistics(request):
    display_chart()
    return render(request, "arch/statistics.html")
