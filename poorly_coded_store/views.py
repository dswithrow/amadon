from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(Product.objects.get(id=request.POST["pid"]).price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    prev_order = 0.00
    try:
        prev_order = float(Order.objects.last().lifetime_spent)
    finally:
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge, lifetime_spent=prev_order+total_charge)
    return redirect("/checkout")

def checkout(request):
    context = {
        "order": Order.objects.last()
    }
    return render(request, "store/checkout.html", context)