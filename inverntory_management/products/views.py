from products.models import Product
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    products = Product.objects.order_by('-created_at')
    context = {"products":products}
    return render(request, 'products/index.html', context)

def detail(request, prod_id):
    try:
        product = Product.objects.get(pk=prod_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'products/details.html', {'prod': product})