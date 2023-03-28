
from django.http import JsonResponse
from data.web_scrapping.isp.awaser.fiber_home import FiberHome
from data.web_scrapping.isp.omantel.heyyak_plus import OmantelHeyyakPlus
from data.web_scrapping.isp.omantel.baqati import OmantelBaqati
# from data.web_scrapping.isp.ooredoo.hala import OoredooHala
from data.web_scrapping.isp.redbull.mobile_plans import RedbullMobilePlans
from data.web_scrapping.isp.rennah.rennah_mobile import RennahMobile
from data.web_scrapping.isp.vodafone.mobilePlans import VodafonePlans
from data.web_scrapping.isp.ooredoo.shahry import OoredooShahry


def data(request):
    fiber_home = FiberHome()
    heyyak_plus = OmantelHeyyakPlus()
    baqati = OmantelBaqati()
    ooredooHala = OoredooShahry()
    mobile_plans = RedbullMobilePlans()
    rennah_mobile = RennahMobile()
    vodafonePlans = VodafonePlans()

    onePlan = True

    data = {
        "Omantel": {
            "heyyak_plus":  heyyak_plus.packages[0] if onePlan else heyyak_plus.packages,
            "baqati": baqati.packages[0] if onePlan else baqati.packages,
        },
        "Redbull": {
            "plans": mobile_plans.packages[0] if onePlan else mobile_plans.packages,
        },
        "Rennah": {
            "plans": rennah_mobile.packages[0] if onePlan else rennah_mobile.packages,
        },
        "Awaser": {
            "plans": fiber_home.packages[0] if onePlan else fiber_home.packages,
        },
        "Ooredoo": {
            # "OoredooHalaPackages": ooredooHala.hala_add_ons_internet_blocks,
            # "OoredooHalaSIMPackages": ooredooHala.hala_SIM_blocks
            "OoredooHalaSIMPackages": ooredooHala.packages
        },
        "Vodafone": {
            "mobile_plans_blocks": vodafonePlans.mobile_plans_blocks,
        },


    }
    return JsonResponse(data)
