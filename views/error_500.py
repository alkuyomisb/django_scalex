from django.shortcuts import render


def error_500(request):
    return render(request, "bestplan/en/errors/500.html")
