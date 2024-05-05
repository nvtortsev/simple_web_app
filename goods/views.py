from django.shortcuts import render, redirect
from .models import Order, Status
from .forms import OrderForm


# получение всех заказов
def get_orders(request):
    # заказы того пользователя, который авторизован
    orders = Order.objects.filter(user=request.user)
    return render(request, "goods/get_orders.html", {"orders": orders})


# создание заказа
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                quantity=form.cleaned_data["quantity"],
                address=form.cleaned_data["address"],
                product=form.cleaned_data["product"],
                status=Status.objects.get(name="Новое"),
                user=request.user,
            )
            order.save()
            return redirect("/goods/get_orders/")
    else:
        form = OrderForm()

    return render(request, "goods/create_order.html", {"form": form})
