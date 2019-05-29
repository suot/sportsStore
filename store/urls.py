from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path(r'<int:cat_no>/', views.detail, name='detail'),
    # path(r'^(?P<cat_no>\d+/)$', views.detail, name='detail'),
]