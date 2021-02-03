from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    users = ["Kristin", "Seth", "Cameron", "Cali", "Bailey"]
    user = request.user
    context = {
        'users': users
    }
    return render(request, "home.html", context)