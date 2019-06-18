from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Client, Order, User
from .forms import OrderForm, InterestForm, ClientForm, LoginForm
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login as sysLogin, logout as sysLogout
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required
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
    if 'last_login' in request.session:
        last_login = 'Last login: ' + request.session['last_login']
    else:
        last_login = 'Your last login was one hour ago'
    cat_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'store/index.html', {'cat_list': cat_list, 'first_name': request.user.first_name, 'last_login': last_login})

@login_required
def about(request):
    if 'about_visits' in request.session:
        request.session['about_visits'] = request.session['about_visits'] + 1
    else:
        request.session['about_visits'] = 1
    return render(request, 'store/about.html', {'first_name': request.user.first_name, 'about_visits': request.session['about_visits']})

@login_required
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
    return render(request, 'store/detail.html', {'category': category, 'products': products, 'cat_no': cat_no, 'first_name': request.user.first_name})

@login_required
def products(request):
    prodlist = Product.objects.all().order_by('id')[:10]
    return render(request, 'store/products.html', {'prodlist': prodlist, 'first_name': request.user.first_name})

@login_required
def place_order(request):
    msg = ''
    prodlist = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.num_units <= order.product.stock:
                order.client = Client.objects.get(username=request.user.username)
                order.save()
                msg = 'Your order has been placed successfully.'
                product = order.product
                product.stock = product.stock - order.num_units
                product.save()
            else:
                msg = 'We do not have sufficient stock to fill your order'
        else:
            msg = 'InvalidError'
        return render(request, 'store/order_response.html', {'msg': msg, 'first_name': request.user.first_name})
    else:
        form = OrderForm()
        return render(request, 'store/placeorder.html', {'form': form, 'msg': msg, 'prodlist': prodlist, 'first_name': request.user.first_name})

@login_required
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
        return render(request, 'store/productdetail.html', {'form': form, 'msg': msg, 'id': product.id, 'first_name': request.user.first_name})


@login_required
def myorders(request):
    client = Client.objects.get(username=request.user.username)
    orderlist = client.order_set.all()
    return render(request, 'store/myorders.html', {'orderlist': orderlist, 'first_name': request.user.first_name})


def register(request):
    msg = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = Client.objects.create_user(username, email, password)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            msg = 'You are registered successfully'
        else:
            msg = 'InvalidError'
        return render(request, 'store/register.html', {'msg': msg})
    else:
        form = ClientForm()
        return render(request, 'store/register.html', {'form': form, 'msg': ''})


def login(request):
    msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    sysLogin(request, user)
                    request.session.set_expiry(300)

                    request.session['last_login'] = str(datetime.datetime.now().replace(microsecond=0))
                    next = request.POST.get('next') #In login.html, a hidden input is used to record the next value and pass it here
                    if next == '':
                        return redirect('/store/')
                        # return redirect(reverse('store:index'))
                    else:
                        return redirect(next)
                else:
                    msg = 'Disabled account'
            else:
                msg = 'Invalid username or password'
        else:
            msg = 'Invalid Error'
        return render(request, 'store/login.html', {'form': form, 'msg': msg})
    else:
        form = LoginForm()
        return render(request, 'store/login.html', {'form': form, 'msg': ''})


@login_required
def logout(request):
    sysLogout(request)
    form = LoginForm()
    return render(request, 'store/login.html', {'form': form, 'msg': ''})
