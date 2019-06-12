from django.urls import path
from store import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about', views.about, name='about'),
    path(r'<int:cat_no>/', views.detail, name='detail'),
    path(r'products', views.products, name='products'),
    path(r'products/<int:prod_id>/', views.productdetail, name='productdetail'),
    path(r'place_order', views.place_order, name='place_order'),
    path(r'register', views.register, name='register')
    # path(r'^(?P<cat_no>\d+/)$', views.detail, name='detail'),
]
