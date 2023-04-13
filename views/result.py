from utils.scalex_toolkit import ScaleXToolkit
from django.shortcuts import render
from utils.database_api import get_one_closest


def result(request):
    price = request.GET.get("price", "all")
    data_allowance = request.GET.get("data_allowance", "all")
    service_type = request.GET.get("service_type", "all")
    plan_type = request.GET.get("plan_type", "all")
    rank = request.GET.get("rank", "all")
    term_length = request.GET.get("term_length", 1)

    isp_list = []
    omantel = request.GET.get("omantel", "off")
    ooredeoo = request.GET.get("ooredeoo", "off")
    vodafone = request.GET.get("vodafone", "off")
    renna = request.GET.get("renna", "off")
    redbull = request.GET.get("redbull", "off")
    awasr = request.GET.get("awasr", "off")

    if "on" in omantel:
        isp_list.append("omantel")
    if "on" in ooredeoo:
        isp_list.append("ooredoo")
    if "on" in vodafone:
        isp_list.append("vodafone")
    if "on" in renna:
        isp_list.append("renna")
    if "on" in redbull:
        isp_list.append("redbull")
    if "on" in awasr:
        isp_list.append("awasr")

    link = ""
    res = {}

    if len(isp_list) == 0:
        plans = {
            "omantel":    get_one_closest({"isp": ["omantel"], "service_type": [service_type], "plan_type": [plan_type]}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "rennah":     get_one_closest({"isp": ["renna"], "service_type": [service_type], "plan_type": [plan_type]}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "ooredoo":    get_one_closest({"isp": ["ooredoo"], "service_type": [service_type], "plan_type": [plan_type]}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "redbull":    get_one_closest({"isp": ["redbull"], "service_type": [service_type], "plan_type": [plan_type]}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "vodafone":   get_one_closest({"isp": ["vodafone"], "service_type": [service_type], "plan_type": [plan_type]}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "friendly":   get_one_closest({"isp": ["friendly"], "service_type": [service_type], "plan_type": [plan_type]}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "awasr":      get_one_closest({"isp": ["awasr"], "service_type": [service_type], "plan_type": [plan_type]}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1)
        }
        res = plans
        link = "bestplan/en/result.html"
    else:
        TOTAL_PLANS_NUMBER = 7
        top_plans = []

        top_plans = get_one_closest({"isp": isp_list,  "service_type": [service_type], "plan_type": [plan_type]}, {
                                    "price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, TOTAL_PLANS_NUMBER),
        res = {"plans": top_plans[0]}
        link = "bestplan/en/top_result.html"

    return render(request, link, res)