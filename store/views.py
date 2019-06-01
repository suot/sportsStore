from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Client, Order
from django.shortcuts import render


# Create your views here.
def index(request):
    # response = HttpResponse()
    #
    # # cat_list = Category.objects.all().order_by('id')[:10]
    # # heading1 = '<p>List of Categories: </p>'
    # # response.write(heading1)
    # # for category in cat_list:
    # #     para = '<p>' + str(category.id) + ': ' + str(category) + '</p>'
    # #     response.write(para)
    #
    # product_list = Product.objects.all().order_by('-price')[:5]
    # heading1 = '<p>List of Products: </p>'
    # response.write(heading1)
    # for product in product_list:
    #     para = '<p>' + str(product.id) + ': ' + str(product) + '</p>'
    #     response.write(para)
    #
    # return response

    cat_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'store/index.html', {'cat_list': cat_list})


def about(request):
    return render(request, 'store/about.html')


def detail(request, cat_no):
    # response = HttpResponse()
    #
    # category = get_object_or_404(Category, id=cat_no)
    # heading = '<p>Category id: ' + str(category.id) + ', Warehouse: ' + str(category.warehouse) + ', and its product list: </p>'
    # response.write(heading)
    #
    # product_list = category.products.all()
    # for product in product_list:
    #     para = '<p>{0}</p>'.format(str(product))
    #     response.write(para)
    # return response

    category = get_object_or_404(Category, id=cat_no)
    products = category.products.all()
    return render(request, 'store/detail.html', {'category': category, 'products': products, 'cat_no': cat_no})