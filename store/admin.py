from django.contrib import admin
from .models import Product, Category, Client, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Order)


def refill_stock(modeladmin, request, queryset):
    for product in queryset:
        product.refill()
refill_stock.short_description = "Refill stock by 50"

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available']
    ordering = ['name']
    actions = [refill_stock]

admin.site.register(Product, ProductAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'get_interested_in', 'avatar']
    ordering = ['first_name']

admin.site.register(Client, ClientAdmin)