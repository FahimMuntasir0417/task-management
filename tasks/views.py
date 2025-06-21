from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(" wel come to the task ")

def contact(request):
    return HttpResponse("<h1>manager</h1>")
def show_task(request):
    return HttpResponse("<h1>manager gsdhjsdjkghrfwgu</h1>")

def show_specific_task(request,id):
    print("id",id)
    print("id type:", type(id))
    return HttpResponse("this is show_specific_task")