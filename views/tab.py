# from data.web_scrapping.isp.ooredoo.hala import OoredooHala

from django.shortcuts import render
def tab(request):
    # data = {
    #     "OoredooHalaPackages": OoredooHala.hala_add_ons_internet_blocks,
    #     "OoredooHalaSIMPackages": OoredooHala.hala_SIM_blocks
    # }
    return render(request, "arch/tab.html", {})
