from django.shortcuts import render

from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def add_book(request):
    return render(request,"add_book.html")


def book_list(request):
    return render(request,"book_list.html")


