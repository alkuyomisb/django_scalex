from django.shortcuts import render
def plans(request):
    return render(request, "arch/plans.html")
