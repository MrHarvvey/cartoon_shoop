from django.shortcuts import render

from .models import *

def store(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'cartoon_shoop/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created =Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items =[]
		order = []
	context = {'items': items, 'order': order}
	return render(request, 'cartoon_shoop/cart.html', context)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created =Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items =[]
		order = []
	context = {'items': items, 'order': order}
	return render(request, 'cartoon_shoop/checkout.html', context)