from django.shortcuts import render
from goods.models import Product


# получение всех товаров
def get_products(request):
	products = Product.objects.all()
	context = {"products": products}

	return render(request, "main/main.html", context)
