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

    link = ""
    res = {}

    if "each" in rank:
        plans = {
            "omantel":    get_one_closest({"isp": "omantel", "service_type": service_type, "plan_type": plan_type}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "rennah":     get_one_closest({"isp": "renna", "service_type": service_type, "plan_type": plan_type}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "ooredoo":    get_one_closest({"isp": "ooredoo", "service_type": service_type, "plan_type": plan_type}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "redbull":    get_one_closest({"isp": "redbull", "service_type": service_type, "plan_type": plan_type}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "vodafone":   get_one_closest({"isp": "vodafone", "service_type": service_type, "plan_type": plan_type}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "friendly":   get_one_closest({"isp": "friendly", "service_type": service_type, "plan_type": plan_type}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1),
            "awasr":      get_one_closest({"isp": "awasr", "service_type": service_type, "plan_type": plan_type}, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 1)
        }
        res = plans
        link = "bestplan/en/result.html"
    else:
        top_plans = get_one_closest({"service_type": service_type, "plan_type": plan_type}, {
                                    "price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, 6),
        res = {"plans": top_plans[0]}
        link = "bestplan/en/top_result.html"

    return render(request, link, res)
