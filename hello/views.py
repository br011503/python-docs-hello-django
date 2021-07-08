from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
#     return HttpResponse("Hello, World!")
def hello(request):
    return render(request, 'hello/table1.html')
