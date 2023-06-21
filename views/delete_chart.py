from django.shortcuts import render
from utils.database_api import delete_chart_and_parameters 
from django.shortcuts import redirect

def delete_chart(request):
    
    chart_id = request.POST.get('chart_id')
    print("chart id: ", chart_id)
    delete_chart_and_parameters(chart_id)


    return redirect('statistics')