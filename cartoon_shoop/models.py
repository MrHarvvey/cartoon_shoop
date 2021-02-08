from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Customer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)


    def __str__(self):
        return str(self.first_name + self.last_name)

class Product(models.Model):
    name = models.CharField(max_length=1000, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True)
    image = models.ImageField(null = True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True)
    transation_id = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.transation_id

    @property
    def get_cart_total_price(self):
        orderitem = self.orderitem_set.all()
        total = sum([item_total.get_total for item_total in orderitem])
        return total

    @property
    def get_total_all_items(self):
        all_items = self.orderitem_set.all()
        total2 = sum([total.quantity for total in all_items])
        return total2
        
    @property
    def zwroc_cokolwiek(self):
        zwroc_cokolwiek = 20000
        return zwroc_cokolwiek
    
    

    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    quantity = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=200, null=True)
    home_number = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    added = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.street