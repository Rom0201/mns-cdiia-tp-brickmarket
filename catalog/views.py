from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>Hello World !</h1>")

def product(request, id:int|None = None ): 

  context = {
    "page_title": "BrickMarket - Lego Super Store",
    "user_name": "Nicolas"
  }

  return render(request, "catalog/product.html", context)