from django.http import JsonResponse
from django.shortcuts import render
from scalex.isp.omantel.heyyak_plus import OmantelHeyyakPlus
from scalex.isp.omantel.baqati import OmantelBaqati
from scalex.isp.ooredoo.shahry import OoredooShahry
from scalex.isp.omantel.tourist_packs import TouristPacks
import csv

from scalex.isp.ooredoo.hala import OoredooHala

heyyak_plus = OmantelHeyyakPlus()
baqati = OmantelBaqati()
shahry = OoredooShahry()
hala = OoredooHala()
tourist_packs = TouristPacks()


def export_packages():
    with open('packages.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Provider",	"Plan Name",	"Plan Type",	"Plan Validity (Days)",	"Total Plan Price",	"Included Data (GB)",	"Promotional Data (GB)",	"Social Media Data (GB)",	"Weekend Data (GB)",
                        "Night Data (GB)",	"Roaming Data (GB)",	"All-Net Minutes",	"On-Net Minutes",	"Weekend Minutes",	"International Minutes",	"All-Net SMS",	"On-Net SMS",	"Notes",	"Plan Web Address"])

        for idx, package in enumerate(heyyak_plus.prices):
            writer.writerow(["Omantel",	"New Hayyak",	"Prepaid",  heyyak_plus.times[idx],	heyyak_plus.prices[idx],
                            heyyak_plus.data_allowance[idx],	"NA",	0,	0,	0,	0,		heyyak_plus.flexi_minutes[idx],	0,	0,	0,	0,	0,	"NA",		prepaid.url])

        for idx, package in enumerate(baqati.prices):
            writer.writerow(["Omantel", baqati.titles[idx],
                             "Pospaid",
                             "",
                             baqati.prices[idx],
                             "-",	"NA",	0,	0,	0,	0,
                             baqati.flexi_minutes[idx],	0,	0,	0,	0,	0,	"NA",
                            baqati.url])


def index(request):
    data = {
        "data_allowance": heyyak_plus.data_allowance,
        "prices": heyyak_plus.prices,
        "times": heyyak_plus.times,
        "social_media_data": heyyak_plus.social_media_data,
        "flexi_minutes": heyyak_plus.flexi_minutes,
        "categories": heyyak_plus.categories,
        "titles": baqati.titles,
        "prices2": baqati.prices,
        "times2": baqati.times,
        "flexi_minutes2": baqati.flexi_minutes,
    }
    return render(request, "index.html", data)


def filter(request):
    return render(request, "bestplan/filter.html")


def result(request):
    return render(request, "bestplan/result.html")


def tab(request):
    data = {
        "OoredooHalaPackages": OoredooHala.hala_add_ons_internet_blocks,
        "OoredooHalaSIMPackages": OoredooHala.hala_SIM_blocks
    }
    return render(request, "arch/tab.html", data)


def tab(request):
    data = {
        "OoredooHalaPackages": OoredooHala.hala_add_ons_internet_blocks,
        "OoredooHalaSIMPackages": OoredooHala.hala_SIM_blocks
    }
    return render(request, "arch/tab.html", data)


def data(request):
    data = {
        "Ooredoo": {
            "OoredooHalaPackages": OoredooHala.hala_add_ons_internet_blocks,
            "OoredooHalaSIMPackages": OoredooHala.hala_SIM_blocks
        },
        "Omantel": {
            "data_allowance": prepaid.data_allowance,
            "prices": prepaid.prices,
            "times": prepaid.times,
            "social_media_data": prepaid.social_media_data,
            "flexi_minutes": prepaid.flexi_minutes,
            "categories": prepaid.categories,
            "titles": baqati.titles,
            "prices2": baqati.prices,
            "times2": baqati.times,
            "flexi_minutes2": baqati.flexi_minutes,
        }


    }
    return JsonResponse(data)


def plans(request):
    return render(request, "arch/plans.html")


def statistics(request):
    return render(request, "arch/statistics.html")
