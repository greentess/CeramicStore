from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator

from store.models.category import Category
from store.models.product import Products


# Create your views here.
class Index(View):
    def get(self, request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        print('cart', request.session['cart'])
        return redirect('homepage')

def store(request):

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    '''----навигация по категориям в каталоге---- '''
    products=None
    categories = Category.get_all_categories()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)