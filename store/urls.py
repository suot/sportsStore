from django.urls import path
from django.conf.urls import url
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('<int:cat_no>/', views.detail, name='detail'),
    path('products', views.products, name='products'),
    path('products/<int:prod_id>/', views.productdetail, name='productdetail'),
    path('place_order', views.place_order, name='place_order'),
    path('myorders', views.myorders, name='myorders'),
    path('register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
