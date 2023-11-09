from django.shortcuts import render
from django.views.generic.base import View
from store.mixins import ProfileMixin
from store.models.customer import Customer

class SaveBuy(ProfileMixin,View):

    def post(self, request):
        customer = Customer.objects.get(user=request.user)
        customer.save()

        return render(request, 'about.html')