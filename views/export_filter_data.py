from utils.scalex_toolkit import ScaleXToolkit
from django.shortcuts import render
from utils.database_api import get_plans
import csv
from django.http import HttpResponse
from utils.database_api import get_plans
from utils.database_api import get_one_closest


def get_merged_value_unit(value, unit):
    if unit == "UNLIMITED":
        return "UNLIMITED"
    else:
        return str(value) + " " + unit


def export_filter_data(request):
    if request.method == "POST":
        request.session["POST"] = request.POST
    else:
        request.POST = request.session["POST"]

    price = request.POST.get("price", "all")
    data_allowance = request.POST.get("data_allowance", "all")
    service_type = request.POST.get("service_type", "all")
    plan_type = request.POST.get("plan_type", "all")
    total_local_minutes = request.POST.get("minutes", "all")
    rank = request.POST.get("rank", "all")
    term_length = request.POST.get("term_length", 1)

    if price == '':
        price = '0'
    if data_allowance == '':
        data_allowance = '0'
    if term_length == '' or term_length == 'all':
        term_length = '0'

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
        not_filter_dict["local_minutes"] = "0"

    # Roaming
    with_roaming = request.POST.get("with_roaming", "off")

    if "on" in with_roaming:
        not_filter_dict["world_roaming_value"] = "0"

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="plans.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(
        [
            '#',
            'ISP',
            'Plan Type',
            'Service Type',
            'Title',
            'Price',
            'Data Allowance',
            'Flexi Minutes',
            'Local Minutes',
            'International Minutes',
            'Fixed Line Minutes',
            'Term Length',
            'Social Media Data',
            'SMS',
            'Download Speed',
            'Upload Speed',
            'Roaming Data',
            'Contact Term Length',
            'Link',
            'Add Ons'
        ])
    stk = ScaleXToolkit()
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
        data = stk.best_plan_merge(plans)
        index = 0
        for key, plan in data.items():
            index += 1
            writer.writerow([

                index,
                plan["isp"],
                plan["plan_type"],
                plan["service_type"],
                plan["title"],

                get_merged_value_unit(plan["price_value"], plan["price_unit"]),
                get_merged_value_unit(
                    plan["data_allowance_value"], plan["data_allowance_unit"]),

                plan["flexi_minutes"],
                plan["local_minutes"],
                plan["international_minutes"],
                plan["fixed_line_minutes"],

                get_merged_value_unit(
                    plan["duration_value"], plan["duration_unit"]),

                get_merged_value_unit(
                    plan["social_media_data_value"], plan["social_media_data_unit"]),

                plan["sms"],

                get_merged_value_unit(
                    plan["download_speed_value"], plan["download_speed_unit"]),

                get_merged_value_unit(
                    plan["upload_speed_value"], plan["upload_speed_unit"]),

                get_merged_value_unit(
                    plan["world_roaming_value"], plan["world_roaming_unit"]),

                get_merged_value_unit(
                    plan["contract_duration_value"], plan["contract_duration_unit"]),

                plan["link"],
                plan["add_on_link"]
            ]
            )

    else:
        TOTAL_PLANS_NUMBER = 7
        top_plans = []

        top_plans = get_one_closest({"isp": isp_list,  "service_type": [service_type], "plan_type": [plan_type]}, not_filter_dict, {
                                    "price_value": price, "data_allowance_value": data_allowance, "duration_value": term_length}, TOTAL_PLANS_NUMBER),
        for index, plan in enumerate(top_plans[0]):
            writer.writerow([
                index,
                plan["isp"],
                plan["plan_type"],
                plan["service_type"],
                plan["title"],

                get_merged_value_unit(plan["price_value"], plan["price_unit"]),
                get_merged_value_unit(
                    plan["data_allowance_value"], plan["data_allowance_unit"]),

                plan["flexi_minutes"],
                plan["local_minutes"],
                plan["international_minutes"],
                plan["fixed_line_minutes"],

                get_merged_value_unit(
                    plan["duration_value"], plan["duration_unit"]),

                get_merged_value_unit(
                    plan["social_media_data_value"], plan["social_media_data_unit"]),

                plan["sms"],

                get_merged_value_unit(
                    plan["download_speed_value"], plan["download_speed_unit"]),

                get_merged_value_unit(
                    plan["upload_speed_value"], plan["upload_speed_unit"]),

                get_merged_value_unit(
                    plan["world_roaming_value"], plan["world_roaming_unit"]),

                get_merged_value_unit(
                    plan["contract_duration_value"], plan["contract_duration_unit"]),

                plan["link"],
                plan["add_on_link"]
            ]
            )

    return response
