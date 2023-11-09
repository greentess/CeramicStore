from django.db import models
from store.models.product import Products
from django.views.generic.base import View
from django.shortcuts import render


class ProductDetailView(View):
    def get(self,request,pk):
        product=Products.objects.get(id=pk)
        return render(request,"card.html",{"product":product})
