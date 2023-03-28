from data.web_scrapping.isp.omantel.heyyak_plus import OmantelHeyyakPlus
from data.web_scrapping.isp.redbull.mobile_plans import RedbullMobilePlans
from data.web_scrapping.isp.vodafone.mobilePlans import VodafonePlans
from data.web_scrapping.isp.ooredoo.shahry import OoredooShahry
from data.web_scrapping.isp.friendly.friendly_mobile import FriendlyMobile
from data.web_scrapping.isp.rennah.rennah_mobile import RennahMobile

from domain.scalex_toolkit import ScaleXToolkit
from django.shortcuts import render


def result(request):
    heyyak_plus = OmantelHeyyakPlus()
    redbull_mobile_plans = RedbullMobilePlans()
    vodafone_mobile_plans = VodafonePlans()
    ooredoo_shahry_plans = OoredooShahry()
    friendly_plans = FriendlyMobile()
    rennah_plans = RennahMobile()

    stk = ScaleXToolkit()

    price = request.GET["price"]
    data_allowance = request.GET["data_allowance"]
    rank = request.GET["rank"]

    plans_dic = {
        "omantel": heyyak_plus.packages,
        "redbull": redbull_mobile_plans.packages,
        "rennah": rennah_plans.packages,
        "vodafone": vodafone_mobile_plans.mobile_plans_blocks,
        "ooredoo": ooredoo_shahry_plans.packages,
        "friendly": friendly_plans.packages,
    }
    filters = {"price": float(price), "data_allowance": float(data_allowance)}

    link = ""
    res = {}

    if "each" in rank:
        plans = stk.get_best_plans_from_each_isp(
            plans_dic,
            filters)
        data = stk.best_plan_merge(plans)
        res = data
        link = "bestplan/result.html"
    else:
        print("->Rennah<-")

        for index, p in enumerate(rennah_plans.packages):
            print("["+str(index)+"]")
            print(p)
            print("-----------------------------")
        top_plans = stk.get_best_plans(
            plans_dic,
            filters)
        top_data = stk.best_plan_list_merge(top_plans)
        print(top_data)
        res = {"plans": top_data}
        link = "bestplan/top_result.html"

    return render(request, link, res)
