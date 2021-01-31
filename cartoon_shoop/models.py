from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Customer(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.email(max_length=200)


	def __str__(self):
		return self.first_name, self.last_name 

class Product(models.Model):
	name = models.CharField(max_length=1000)
	price = models.FloatField()
	digital = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	name_order = models.CharField(max_length=1000)


