from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return redirect('/')

    return render(request, "login/login.html")

def register(request: HttpRequest) -> HttpResponse:
    return render(request, "login/register.html")