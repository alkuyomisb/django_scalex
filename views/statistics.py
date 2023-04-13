from django.shortcuts import render
def statistics(request):
    return render(request, "arch/statistics.html")
