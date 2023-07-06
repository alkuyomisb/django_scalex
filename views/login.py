from django.shortcuts import render
from utils.database_api import get_users
import json

def login(request):
    users = get_users()
    js_users = json.dumps(users)
    
    return render(request, "auth/login.html", {"users" : js_users})