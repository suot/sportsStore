from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Client, Order


# Create your views here.
def index(request):
    response = HttpResponse()

    # cat_list = Category.objects.all().order_by('id')[:10]
    # heading1 = '<p>List of Categories: </p>'
    # response.write(heading1)
    # for category in cat_list:
    #     para = '<p>' + str(category.id) + ': ' + str(category) + '</p>'
    #     response.write(para)

    product_list = Product.objects.all().order_by('-price')[:5]
    heading1 = '<p>List of Products: </p>'
    response.write(heading1)
    for product in product_list:
        para = '<p>' + str(product.id) + ': ' + str(product) + '</p>'
        response.write(para)

    return response

def about(request):
    response = HttpResponse()
    heading1 = '<p>This is an Online Store APP.</p>'
    response.write(heading1)
    return response

def detail(request, cat_no):
    response = HttpResponse()

    category = get_object_or_404(Category, pk=cat_no)
    heading = '<p>Category id: ' + str(category.id) + ', Warehouse: ' + str(category.warehouse) + ', and its product list: </p>'
    response.write(heading)

    product_list = category.products.all()
    for product in product_list:
        para = '<p>{0}</p>'.format(str(product))
        response.write(para)
    return response