from django.http import HttpResponse
from django.shortcuts import render
from scalex.isp.omantel.prepaid import OmantelPrepaid
from scalex.isp.omantel.baqati import OmantelBaqati
from scalex.isp.ooredoo.shahry import OoredooShahry
import csv

prepaid = OmantelPrepaid()
baqati = OmantelBaqati()
shahry = OoredooShahry()

def export_packages():
    with open('packages.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Provider",	"Plan Name",	"Plan Type",	"Plan Validity (Days)",	"Total Plan Price",	"Included Data (GB)",	"Promotional Data (GB)",	"Social Media Data (GB)",	"Weekend Data (GB)",	"Night Data (GB)",	"Roaming Data (GB)",	"All-Net Minutes",	"On-Net Minutes",	"Weekend Minutes",	"International Minutes",	"All-Net SMS",	"On-Net SMS",	"Notes",	"Plan Web Address"])
        
        for idx, package in enumerate(prepaid.prices):
                writer.writerow(["Omantel",	"New Hayyak",	"Prepaid",  prepaid.times[idx],	prepaid.prices[idx],	prepaid.data_allowance[idx],	"NA",	0,	0,	0,	0,		prepaid.flexi_minutes[idx],	0,	0,	0,	0,	0,	"NA",		prepaid.url ])

        for idx, package in enumerate(baqati.prices):
                writer.writerow(["Omantel", baqati.titles[idx],	
                "Pospaid", 
                 "",
                 	baqati.prices[idx],
                	"-",	"NA",	0,	0,	0,	0,	
                    	baqati.flexi_minutes[idx],	0,	0,	0,	0,	0,	"NA",	
                        	baqati.url ])

   


# baqati.times[idx]
# baqati.data_allowance[idx]
def index(request):
    # export_packages()
    data = {
        "data_allowance": prepaid.data_allowance ,
        "prices": prepaid.prices ,
        "times": prepaid.times ,
        "social_media_data": prepaid.social_media_data ,
        "flexi_minutes": prepaid.flexi_minutes ,
        "categories": prepaid.categories ,
        "titles": baqati.titles ,
        "prices2": baqati.prices ,
        "times2": baqati.times ,
        "flexi_minutes2": baqati.flexi_minutes ,
    }
    return render(request, "index.html" , data)


def filter(request):
    # export_packages()
    data1 = {
        "data_allowance": prepaid.data_allowance ,
        "prices": prepaid.prices ,
        "times": prepaid.times ,
        "social_media_data": prepaid.social_media_data ,
        "flexi_minutes": prepaid.flexi_minutes ,
        "categories": prepaid.categories ,
        "titles": baqati.titles ,
        "prices2": baqati.prices ,
        "times2": baqati.times ,
        "flexi_minutes2": baqati.flexi_minutes ,
    }
    return render(request, "bestplan/filter.html" , data1)



def result(request):
    # export_packages()
    data2 = {
        "data_allowance": prepaid.data_allowance ,
        "prices": prepaid.prices ,
        "times": prepaid.times ,
        "social_media_data": prepaid.social_media_data ,
        "flexi_minutes": prepaid.flexi_minutes ,
        "categories": prepaid.categories ,
        "titles": baqati.titles ,
        "prices2": baqati.prices ,
        "times2": baqati.times ,
        "flexi_minutes2": baqati.flexi_minutes ,
    }
    return render(request, "bestplan/result.html" , data2)

def tab(request):
    # export_packages()
    data2 = {
        "data_allowance": prepaid.data_allowance ,
        "prices": prepaid.prices ,
        "times": prepaid.times ,
        "social_media_data": prepaid.social_media_data ,
        "flexi_minutes": prepaid.flexi_minutes ,
        "categories": prepaid.categories ,
        "titles": baqati.titles ,
        "prices2": baqati.prices ,
        "times2": baqati.times ,
        "flexi_minutes2": baqati.flexi_minutes ,
    }
    return render(request, "arch/tab.html" , data2)

def plans(request):
    # export_packages()
    data3 = {
        "data_allowance": prepaid.data_allowance ,
        "prices": prepaid.prices ,
        "times": prepaid.times ,
        "social_media_data": prepaid.social_media_data ,
        "flexi_minutes": prepaid.flexi_minutes ,
        "categories": prepaid.categories ,
        "titles": baqati.titles ,
        "prices2": baqati.prices ,
        "times2": baqati.times ,
        "flexi_minutes2": baqati.flexi_minutes ,
    }
    return render(request, "arch/plans.html" , data3)

def statistics(request):
    # export_packages()
    data4 = {
        "data_allowance": prepaid.data_allowance ,
        "prices": prepaid.prices ,
        "times": prepaid.times ,
        "social_media_data": prepaid.social_media_data ,
        "flexi_minutes": prepaid.flexi_minutes ,
        "categories": prepaid.categories ,
        "titles": baqati.titles ,
        "prices2": baqati.prices ,
        "times2": baqati.times ,
        "flexi_minutes2": baqati.flexi_minutes ,
    }
    return render(request, "arch/statistics.html" , data4)



    

