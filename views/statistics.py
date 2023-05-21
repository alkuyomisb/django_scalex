from django.shortcuts import render
from utils.database_api import get_all_plans
from utils.database_api import get_axis_list
from utils.database_api import get_all_charts
from utils.database_api import get_chart_dict
import json
def statistics(request):
    plans = get_all_plans()
    # axis = get_axis_list("international_minutes")
    # all_charts = get_all_charts()
    chart_dict = get_chart_dict()
    js_data = json.dumps(chart_dict)


    return render(request, "arch/statistics.html" , {"plans":plans , "charts" :js_data   })
