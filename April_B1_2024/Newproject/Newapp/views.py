from django.shortcuts import render
from django.http import HttpResponse
def Myfunction(request):
    return HttpResponse("Introduction to Django")
def Newfunction(request):
    return HttpResponse("WELCOME")
def intropage(request):
    return render(request,"Introduction.html")
def demofunction(request):
    return render(request,"demo.html")

# Create your views here.
