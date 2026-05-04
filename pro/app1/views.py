from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#class based view

#def home(request):
 #   return HttpResponse("Welcome To Django")

#d#ef index(request):
  #  return HttpResponse("Index Page")

def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')