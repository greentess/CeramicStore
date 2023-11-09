"""CeramicVibes11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from store.views.home import Index, store
from store.views.signup import Signup
from store.views.login import Login, logout
from store.views.cart import Cart
from store.views.checkout import CheckOut
from store.views.orders import OrderView
from store.views.about import about
from store.views.contacts import contacts
from store.views.product import ProductDetailView
from store.middlewares.auth import auth_middleware
from django.conf import settings
from django.conf.urls.static import static

from store.views import save
from store.views import email_success

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', Index.as_view(), name='homepage'),
                  path('store', store, name='store'),
                  path('signup', Signup.as_view(), name='signup'),
                  path('login', Login.as_view(), name='login'),
                  path('logout', logout, name='logout'),
                  path('cart', Cart.as_view(), name='cart'),
                  path('check-out', CheckOut.as_view(), name='checkout'),
                  path('orders', auth_middleware(OrderView.as_view()), name='orders'),
                  path('about', about, name='about'),
                  path('about/', about, name='about'),
                  path('contacts', contacts, name='contacts'),
                  path('<int:pk>/', ProductDetailView.as_view()),

                  #path('about/', save.SaveBuy.as_view(), name="update_customer_after"),
                  path('accounts/',include('allauth.urls')),
                  path ('accessions/', include ('allauth.urls')),

                  #path('email_success/', save.email_success, name='email_success')

                  path('email_success/', email_success.SaveBuy.as_view(), name="update_customer_after"),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
