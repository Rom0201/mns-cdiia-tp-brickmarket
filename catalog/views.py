from django.shortcuts import render
from django.http import HttpResponse

def product(request, id:int|None = None ): 

  context = {
    "page_title": "BrickMarket - Lego Super Store",
    "user_name": "Nicolas",
    "product": {
      "id": id,
      "name": "LEGO Star Wars: The Mandalorian The Razor Crest 75292",
      "price": 129.99,
      "description": "The Razor Crest is a LEGO Star Wars set that allows fans to build and play with the iconic ship from the popular TV series, The Mandalorian. This set features a detailed design, including a cockpit, cargo hold, and minifigures of the Mandalorian and other characters.",
      "image_url": "https://m.media-amazon.com/images/I/81gnlmQ5NUL._AC_SX679_.jpg"
    }
  }

  return render(request, "catalog/product.html", context)