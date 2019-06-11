from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Client, Order
from .forms import OrderForm, InterestForm
from django.shortcuts import redirect

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


def products(request):
    prodlist = Product.objects.all().order_by('id')[:10]
    return render(request, 'store/products.html', {'prodlist': prodlist})


def place_order(request):
    msg = ''
    prodlist = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.num_units <= order.product.stock:
                order.save()
                msg = 'Your order has been placed successfully.'
                product = order.product
                product.stock = product.stock - order.num_units
                product.save()
            else:
                msg = 'We do not have sufficient stock to fill your order.'
        else:
            msg = 'InvalidError.'
        return render(request, 'store/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
        return render(request, 'store/placeorder.html', {'form': form, 'msg': msg, 'prodlist': prodlist})


def productdetail(request, prod_id):
    msg = ''
    product = Product.objects.get(id=prod_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['interested']==1:
                product.interested += 1
                product.save()
        return redirect('/store/')
    else:
        form = InterestForm()
        if product.available == True:
            msg = "Name: " + product.name + ", Interesed: " + str(product.interested) + ", Price: " + str(product.price)
        else:
            msg = "Product is not available."
        return render(request, 'store/productdetail.html', {'form': form, 'msg': msg, 'id': product.id})
