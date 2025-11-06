from django.shortcuts import render
from .models import Product

def scan_product(request):
    product = None
    if request.method == "POST":
        upc = request.POST.get("upc")
        product = Product.objects.filter(upc=upc).first()
    return render(request, "scan.html", {"product": product})
