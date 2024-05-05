from django.urls import path
from . import views

# чтобы увидел urls.py проекта
app_name = "main"
urlpatterns = [path("", views.get_products, name="get_products")]
