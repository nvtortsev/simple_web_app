from django.urls import path
from . import views

# чтобы увидел urls.py проекта
app_name = "goods"
urlpatterns = [
    path("get_orders/", views.get_orders, name="get_orders"),
    path("create_order/", views.create_order, name="create_order"),
]
