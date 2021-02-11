from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse

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

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('action', action)
	print('productid', productId)
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created =Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	print(orderItem, created)
	if action == 'add':
		orderItem.quantity =+ 1 
	elif action == 'remove':
		orderItem.quantity =- 1 
	orderItem.safe()

	if orderItem.quantity <= 0:
		orderItem.delete()
		




	return JsonResponse('Item was added', safe=False)