from django.shortcuts import render


def index(request):
    data = {}
    lang = request.GET.get("lang", "en")

    return render(
        request,
        "bestplan/{}/filter.html".format(lang), data)
