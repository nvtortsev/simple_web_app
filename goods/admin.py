from django.contrib import admin
from .models import Product, Order, Status

# Register your models here.
admin.site.register([Product, Order, Status])
