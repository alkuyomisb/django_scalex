from django.shortcuts import render


def index(request):
    data = {}
    print('indexing...')
    # return render(
    #     request,
    #     "bestplan/en/mobile_form.html", data)
    return render(
        request,
        "bestplan/en/filter.html", data)
