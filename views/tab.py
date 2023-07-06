# from data.web_scrapping.isp.ooredoo.hala import OoredooHala
from utils.database_api import get_all_plans
from utils.database_api import get_charts
import json

from django.shortcuts import render
def tab(request):
    plans = get_all_plans()
    chart_result = get_charts()
    js_data = json.dumps(chart_result)
    return render(request, "arch/tab.html", {"plans": plans , "charts" : js_data})
