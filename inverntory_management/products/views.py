from products.models import Product
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    products = Product.objects.order_by('-created_at')
    context = {"products": products}
    return render(request, 'products/index.html', context)


def detail(request, prod_id):
    try:
        product = Product.objects.get(pk=prod_id)
    except Product.DoesNotExist:
        return render(request, 'products/error.html', {'error': {'error_code':404, 'error_message':'Product not found '}})

    return render(request, 'products/details.html', {'prod': product})
