from django.shortcuts import render
from utils.database_api import get_all_plans
from utils.database_api import get_charts

import json
def statistics(request):
    plans = get_all_plans()
    chart_result = get_charts()
    js_data = json.dumps(chart_result)
    print("data from statistics page: ", js_data)

    
    return render(request, "arch/statistics.html" , {"plans":plans , "charts":js_data })
