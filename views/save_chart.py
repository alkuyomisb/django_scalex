from django.shortcuts import render
from utils.database_api import add_chart
def save_chart(request):
    
    chartType = request.GET.get("chartType")
    xAxis = request.GET.get("xAxis")
    yAxis = request.GET.get("yAxis")
    add_chart( chartType , xAxis , yAxis )

    return render(request, "arch/statistics.html" )