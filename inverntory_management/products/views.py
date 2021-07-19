
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from products.models import Product
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string



@login_required(login_url='/accounts/login')
def index(request):
    products = Product.objects.order_by('-created_at')
    context = {"products": products}
    return render(request, 'products/index.html', context)

@login_required(login_url='/accounts/login/')
def detail(request, prod_id):
    try:
        product = Product.objects.get(pk=prod_id)
    except Product.DoesNotExist:
        return render(request, 'products/error.html', {'error': {'error_code': 404, 'error_message': 'Product not found '}})

    return render(request, 'products/details.html', {'prod': product})

@login_required(login_url='/accounts/login')
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

def detail(request, prod_id):
    try:
        product = Product.objects.get(pk=prod_id)
    except Product.DoesNotExist:
        return render(request, 'products/error.html', {'error': {'error_code':404, 'error_message':'Product not found '}})

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

@login_required(login_url='/accounts/login')
def update_product(request):
    # id = request.post.get('id')
    # prod = Product.objects.get(pk=id)
    # prod.name = request.post.get('name')
    # prod.company_name = request.post.get('company_name')
    # prod.price = request.post.get('price')
    # prod.description = request.post.get('description')
    # # save modified product
    # prod.save()

    if request.method == 'POST':
        id = request.GET.get('q')
        model = Product.objects.get(pk=id)
        form = ProductForm(request.POST, instance=model)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('/products/')
    else:
        id = request.GET.get('q')
        prod = Product.objects.get(pk=id)
        form = ProductForm(instance=prod)
        return render(request, 'products/edit.html', {'form': form, 'ctx':str(id)})

@login_required(login_url='/accounts/login')
def add_product(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.created_by = request.user
            new_product.save()
            return redirect('/products/')
    else:
        form = ProductForm()
        return render(request, 'products/edit.html', {'form': form})
