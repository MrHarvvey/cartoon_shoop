from django.shortcuts import render

from .models import *

def store(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'cartoon_shoop/store.html', context)

def cart(request):
	context = {}
	return render(request, 'cartoon_shoop/cart.html', context)


def checkout(request):
	context = {}
	return render(request, 'cartoon_shoop/checkout.html', context)