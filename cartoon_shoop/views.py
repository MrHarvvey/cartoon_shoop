from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'cartoon_shoop/store.html', context)

def cart(request):
	context = {}
	return render(request, 'cartoon_shoop/cart.html', context)


def checkout(request):
	context = {}
	return render(request, 'cartoon_shoop/checkout.html', context)