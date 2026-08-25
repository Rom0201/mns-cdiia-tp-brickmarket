from django.urls import path
# from .view import add, add, remove, ...
from . import views

# (% url 'cart:add' %)
app_name = "cart"

urlpatterns = [
    path("", views.view_cart, name="view"),
    path("add/", views.add, name="add"),
    path("set_quantity", views.set_quantity, name="set_quantity"),
    path("delete", views.delete, name="delete"),
    path("clear", views.clear, name="clear")
]

