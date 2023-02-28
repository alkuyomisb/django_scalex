from scalex.isp.omantel.heyyak_plus import OmantelHeyyakPlus
from scalex.isp.omantel.baqati import OmantelBaqati
from scalex.isp.ooredoo.shahry import OoredooShahry
from scalex.isp.omantel.tourist_packs import TouristPacks
from scalex.isp.awaser.fiber_home import FiberHome
import csv
from scalex.isp.ooredoo.hala import OoredooHala
from scalex.scalex_toolkit import ScaleXToolkit
from scalex.isp.redbull.mobile_plans import MobilePlans
from scalex.isp.rennah.rennah_mobile import RennahMobile

stk = ScaleXToolkit()
heyyak_plus = OmantelHeyyakPlus()
# baqati = OmantelBaqati()
# shahry = OoredooShahry()
# hala = OoredooHala()
# fiber_home = FiberHome()
# tourist_packs = TouristPacks()
mobile_plans = MobilePlans()
# rennah_mobile = RennahMobile()
# print(stk.get_best_plans(heyyak_plus.packages,
#       {"price": 2, "data_allowance": 5}))
print(mobile_plans.packages)
# print(heyyak_plus.packages)


# def export_packages():
#     with open('packages.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Provider",	"Plan Name",	"Plan Type",	"Plan Validity (Days)",	"Total Plan Price",	"Included Data (GB)",	"Promotional Data (GB)",	"Social Media Data (GB)",	"Weekend Data (GB)",
#                         "Night Data (GB)",	"Roaming Data (GB)",	"All-Net Minutes",	"On-Net Minutes",	"Weekend Minutes",	"International Minutes",	"All-Net SMS",	"On-Net SMS",	"Notes",	"Plan Web Address"])

# for idx, package in enumerate(heyyak_plus.packages):
#     writer.writerow(["Omantel",
#                     "New Heyyak",
#                      "Prepaid",
#                      stk.merge_value_and_unit(package["duration"]),
#                      stk.merge_value_and_unit(package["price"]),
#                      stk.merge_value_and_unit(package["data_allowance"]),	"NA",	stk.merge_value_and_unit(package["social_media_data"]),	0,	0,	0,		"Prom data",	0,	0,	0,	0,	0,	"NA",		heyyak_plus.HEYYAK_PLUS_URL])

# for idx, package in enumerate(tourist_packs.packages):
#     writer.writerow(["Omantel",
#                     "Tourist Packs",
#                      "Prepaid",
#                      stk.merge_value_and_unit(package["duration"]),
#                      stk.merge_value_and_unit(package["price"]),
#                      stk.merge_value_and_unit(package["data_allowance"]),	"NA",	"Social Media Data",	0,	0,	0,		"Prom data",	0,	0,	0,	0,	0,	"NA",		tourist_packs.TOURIST_PACKS_URL])

# for idx, package in enumerate(heyyak_plus.packages):
#     writer.writerow(["Omantel",
#                     "Baqati",
#                      "Prepaid",
#                      stk.merge_value_and_unit(package["duration"]),
#                      stk.merge_value_and_unit(package["price"]),
#                      stk.merge_value_and_unit(package["data_allowance"]),	"NA",	stk.merge_value_and_unit(package["social_media_data"]),	0,	0,	0,		"Prom data",	0,	0,	0,	0,	0,	"NA",		heyyak_plus.HEYYAK_PLUS_URL])

# for idx, package in enumerate(mobile_plans.packages):
#     writer.writerow(["Redbull",
#                     "Mobile Plan",
#                      "Prepaid",
#                      stk.merge_value_and_unit(package["duration"]),
#                      stk.merge_value_and_unit(package["price"]),
#                      stk.merge_value_and_unit(package["included_data"]),	"NA",	0,	0,	0,	0,		"Prom data",	0,	0,	0,	0,	0,	"NA",		mobile_plans.MOBILE_PLANS_URL])

# for idx, package in enumerate(fiber_home.packages):
#     writer.writerow(["Awaser",
#                     "Fiber Home",
#                      "Postpaid",
#                      "duration",
#                      stk.merge_value_and_unit(package["price"]),
#                      "Unlimited",	"NA",	0,	0,	0,	0,		"Prom data",	0,	0,	0,	0,	0,	"NA",		fiber_home.FIBER_HOME_URL])


# export_packages()
def index(request):
    data = {
        # "data_allowance": heyyak_plus.data_allowance,
        # "prices": heyyak_plus.prices,
        # "times": heyyak_plus.times,
        # "social_media_data": heyyak_plus.social_media_data,
        # "flexi_minutes": heyyak_plus.flexi_minutes,
        # "categories": heyyak_plus.categories,
        # "titles": baqati.titles,
        # "prices2": baqati.prices,
        # "times2": baqati.times,
        # "flexi_minutes2": baqati.flexi_minutes,
    }
    return render(request, "index.html", data)


def filter(request):
    return render(request, "bestplan/filter.html")


def result(request):
    return render(request, "bestplan/result.html")


# def tab(request):
#     data = {
#         "OoredooHalaPackages": OoredooHala.hala_add_ons_internet_blocks,
#         "OoredooHalaSIMPackages": OoredooHala.hala_SIM_blocks
#     }
#     return render(request, "arch/tab.html", data)


# def tab(request):
#     data = {
#         "OoredooHalaPackages": OoredooHala.hala_add_ons_internet_blocks,
#         "OoredooHalaSIMPackages": OoredooHala.hala_SIM_blocks
#     }
#     return render(request, "arch/tab.html", data)


# def data(request):
#     data = {
#         "Ooredoo": {
#             "OoredooHalaPackages": OoredooHala.hala_add_ons_internet_blocks,
#             "OoredooHalaSIMPackages": OoredooHala.hala_SIM_blocks
#         },
#         "Omantel": {
#             "data_allowance": prepaid.data_allowance,
#             "prices": prepaid.prices,
#             "times": prepaid.times,
#             "social_media_data": prepaid.social_media_data,
#             "flexi_minutes": prepaid.flexi_minutes,
#             "categories": prepaid.categories,
#             "titles": baqati.titles,
#             "prices2": baqati.prices,
#             "times2": baqati.times,
#             "flexi_minutes2": baqati.flexi_minutes,
#         }


#     }
#     return JsonResponse(data)


# def plans(request):
#     return render(request, "arch/plans.html")


# def statistics(request):
#     return render(request, "arch/statistics.html")
