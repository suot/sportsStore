from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    warehouse = models.CharField(max_length=200, default='Windsor')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    interested = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def refill(self):
        self.stock += 50
        self.save()

class Client(User):
    PROVINCE_CHOICES = [
        ('AB', 'Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec')
    ]
    company = models.CharField(max_length=50, blank=True)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    interested_in = models.ManyToManyField(Category)
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_interested_in(self):
        return "\n".join([c.name for c in self.interested_in.all()])

class Order(models.Model):
    STATUS_CHOICES = [
        (0, 'Order Cancelled'),
        (1, 'Order Placed'),
        (2, 'Order Shipped'),
        (3, 'Order Delivered')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    num_units = models.PositiveIntegerField(default=1)
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    status_date = models.DateField(default=datetime.date.today())

    def total_cost(self):
        return self.product.price * self.num_units

    def __str__(self):
        return 'Product: ' + self.product.name + '. Total cost: ' + str(self.total_cost())