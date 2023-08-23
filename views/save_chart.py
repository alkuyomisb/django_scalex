from django.shortcuts import render
from utils.database_api import add_chart
from django.shortcuts import redirect

def save_chart(request):
    query_params = request.GET
    chartType = request.GET.get("chartType")
    plan_fields = query_params.getlist("plan_field")
    add_chart(chartType, plan_fields)


    return redirect('tab')