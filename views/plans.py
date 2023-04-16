from django.shortcuts import render
from utils.database_api import get_all_plans
def plans(request):
    plans = get_all_plans()
    print(plans)
    return render(request, "arch/plans.html" , {"plans":plans})
