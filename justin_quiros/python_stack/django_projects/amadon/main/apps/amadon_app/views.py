from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	if request.session.get('total') == None:
		request.session['total'] = 0
	if request.session.get('charged') ==None:
		request.session['charged'] = 0
	if request.session.get('qty') == None:
		request.session['qty'] = 0

	store = [{
	"id": 0,
	"item": "Dojo Tshirt",
	"price": "19.99"
	},
	{
	"id": 1,
	"item": "Dojo Sweater",
	"price": "29.99"
	},
	{
	"id": 2,
	"item": "Dojo Cup",
	"price": "4.99"
	},
	{
	"id": 3,
	"item": "Algorithm Book",
	"price": "49.99"
	}]

	request.session['price_list'] = [19.99, 29.99, 4.99, 49.99]

	request.session['store'] = store

	return render(request, 'amadon_app/index.html')

def process(request):
	i = int(request.POST['product_id'])
	charged = float(request.session['price_list'][i]) * int(request.POST['quantity'])
	request.session['charged'] = charged
	request.session['total'] = int(request.session['total']) + int(request.session['charged'])
	request.session['qty'] = int(request.session['qty']) + int(request.POST['quantity'])


	return redirect('/checkout')


def checkout(request):
	return render(request, 'amadon_app/checkout.html')

def clear(request):
	del request.session['qty']
	return redirect('/')