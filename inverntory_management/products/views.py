
from django.http.response import JsonResponse
from products.models import Product
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

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
        return render(request, 'products/error.html', {'error': {'error_code': 404, 'error_message': 'Product not found '}})

    return render(request, 'products/details.html', {'prod': product})

def product_search(request):
    url_param = request.GET.get('q')
    if url_param:
        products = Product.objects.filter(name__icontains=url_param)
    else:
        products = Product.objects.all()
    
    data = render_to_string(
        template_name = 'products/products_partial.html',
        context = {'products':products}
    )
    data_dict = {'html_from_view': data}
    return JsonResponse(data=data_dict, safe=False)

