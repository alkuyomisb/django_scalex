from utils.scalex_toolkit import ScaleXToolkit
from django.shortcuts import render
from utils.database_api import get_one_closest


def result(request):
    price = request.POST.get("price", "all")
    data_allowance = request.POST.get("data_allowance", "all")
    service_type = request.POST.get("service_type", "all")
    plan_type = request.POST.get("plan_type", "all")
    total_local_minutes = request.POST.get("minutes", "all")
    rank = request.POST.get("rank", "all")
    term_length = request.POST.get("term_length", 30)
    lang = request.POST.get("lang", 'en')

    if price == '':
        price = '0'
    if data_allowance == '':
        data_allowance = '0'
    if term_length == '' or term_length == 'all':
        term_length = '0'

    # Operators
    isp_list = []
    omantel = request.POST.get("omantel", "off")
    ooredeoo = request.POST.get("ooredeoo", "off")
    vodafone = request.POST.get("vodafone", "off")
    renna = request.POST.get("renna", "off")
    redbull = request.POST.get("redbull", "off")
    awasr = request.POST.get("awasr", "off")

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

    # Minutes
    not_filter_dict = {}
    international_minutes = request.POST.get("international_minutes", "off")
    local_minutes = request.POST.get("local_minutes", "off")

    if "on" in international_minutes:
        not_filter_dict["international_minutes"] = "0"

    if "on" in local_minutes:
        not_filter_dict["total_local_minutes"] = "0.0"

    # Roaming
    with_roaming = request.POST.get("with_roaming", "off")

    if "on" in with_roaming:
        not_filter_dict["world_roaming_value"] = "0"

    link = ""
    res = {}

    if len(isp_list) == 0:
        plans = {
            "omantel":    get_one_closest({"isp": ["omantel"], "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length, "total_local_minutes": total_local_minutes}, 1),
            "rennah":     get_one_closest({"isp": ["renna"], "service_type": [service_type], "plan_type":   [plan_type]},  not_filter_dict,  {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length, "total_local_minutes": total_local_minutes}, 1),
            "ooredoo":    get_one_closest({"isp": ["ooredoo"], "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length, "total_local_minutes": total_local_minutes}, 1),
            "redbull":    get_one_closest({"isp": ["redbull"], "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length, "total_local_minutes": total_local_minutes}, 1),
            "vodafone":   get_one_closest({"isp": ["vodafone"], "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length, "total_local_minutes": total_local_minutes}, 1),
            "friendly":   get_one_closest({"isp": ["friendly"], "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length, "total_local_minutes": total_local_minutes}, 1),
            "awasr":      get_one_closest({"isp": ["awasr"], "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {"price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length, "total_local_minutes": total_local_minutes}, 1)
        }
        res = plans
        link = "bestplan/{}/result.html".format(lang)
    else:
        TOTAL_PLANS_NUMBER = 7
        top_plans = []

        top_plans = get_one_closest({"isp": isp_list,  "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {
                                    "price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, TOTAL_PLANS_NUMBER),
        res = {"plans": top_plans[0]}
        link = "bestplan/{}/top_result.html".format(lang)

    return render(request, link, res)
