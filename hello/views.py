from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
#     return HttpResponse("Hello, World!")

def index(request):
    return render(request, "tables/table1.html")
