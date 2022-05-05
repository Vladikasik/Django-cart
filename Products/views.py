from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    return render(request, 'main.html', {"products": all_products})

def cart(request):
    cart = request.session['cart']
    cart = [Product.objects.get(pk=id) for id in cart]
    print(cart)
    return render(request, 'cart.html', {'cart': cart})

def add_product(request, id):
    session = request.session
    try:
        session['cart'].append(id)
    except:
        session['cart'] = [id]
    return HttpResponse('<script type="text/javascript">window.close()</script>')  